import yaml
import os
import glob
import utils as ut

class merger():

#__________________________________________________________
    def __init__(self, process, yamldir, version):
        self.indir = yamldir+version
        self.process = process
#__________________________________________________________
    def merge(self, force):
        
        print self.indir,'  ====  ',self.process
        ldir=[x[0] for x in os.walk(self.indir)]
        process = ''
        for l in ldir:
            process = l.replace(self.indir,"")
            if self.process!='' and self.process!=process: 
                continue
            outfile=l+'/merge.yaml'
            totsize=0
            totevents=0
            outfiles=[]
            outfilesbad=[]
            users={}
            outdir=None
            ndone=0
            nbad=0
            All_files = glob.glob("%s/output_*.yaml"%(l))
            if len(All_files)==0:
                if os.path.isfile("%s/merge.yaml"%(l)):
                    os.system("rm %s/merge.yaml"%(l))
                continue

            #continue if process has been checked
            print '%s/check'%(l)
            if not ut.file_exist('%s/check'%(l)) and not force: continue


            print 'merging %i files in directory %s'%(len(All_files), l)
            for f in All_files:
                if not os.path.isfile(f): 
                    print 'file does not exists... %s'%f
                    continue
                
                with open(f, 'r') as stream:
                    try:
                        tmpf = yaml.load(stream) 
                        if ut.getsize(f)==0: 
                            os.system("rm %s"%(f))
                            continue
                        if ut.getsize(f)==0: continue
                        if tmpf['processing']['status']=='sending': continue
                        if tmpf['processing']['status']=='BAD':
                            nbad+=1
                            outfilesbad.append(tmpf['processing']['out'].split('/')[-1])
                            outdir=tmpf['processing']['out'].replace(tmpf['processing']['out'].split('/')[-1],'')
                            process=tmpf['processing']['process']
                            continue

                        totsize+=tmpf['processing']['size']
                        totevents+=tmpf['processing']['nevents']
                        process=tmpf['processing']['process']
                        tmplist=[tmpf['processing']['out'].split('/')[-1], tmpf['processing']['nevents']]
                        outfiles.append(tmplist)
                        outdir=tmpf['processing']['out'].replace(tmpf['processing']['out'].split('/')[-1],'')
                        if tmpf['processing']['user'] not in users: users[tmpf['processing']['user']]=1
                        else: users[tmpf['processing']['user']]=users[tmpf['processing']['user']]+1
                        ndone+=1
                    except yaml.YAMLError as exc:
                        print(exc)
                        
            dic = {'merge':{
                    'process':process, 
                    'nevents':totevents,
                    'outfiles':outfiles,
                    'outdir':outdir,
                    'size':totsize,
                    'ndone':ndone,
                    'nbad':nbad,
                    'outfilesbad':outfilesbad,
                    'users':users
                    }
                   }
            try:
                with open(outfile, 'w') as outyaml:
                    yaml.dump(dic, outyaml, default_flow_style=False) 
            except IOError as exc:
                print "I/O error({0}): {1}".format(exc.errno, exc.strerror)
                print "outfile ",outfile
                import time
                time.sleep(10)
                with open(outfile, 'w') as outyaml:
                    yaml.dump(dic, outyaml, default_flow_style=False)


