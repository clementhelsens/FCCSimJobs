! main03.cmnd.
! This file contains commands to be read in for a Pythia8 run.
! Lines not beginning with a letter or digit are comments.
! Names are case-insensitive  -  but spellings-sensitive!
! The settings here are illustrative, not always physics-motivated.

! 1) Settings used in the main program.
Random:setSeed = on
Random:seed = 0

Main:numberOfEvents = 1000         ! number of events to generate
Main:timesAllowErrors = 100          ! how many aborts before run stops

! 2) Settings related to output in init(), next() and stat().
Init:showChangedSettings = on      ! list changed settings
Init:showChangedParticleData = off ! list changed particle data
Next:numberCount = 100             ! print message every n events
Next:numberShowInfo = 1            ! print event information n times
Next:numberShowProcess = 1         ! print process record n times
Next:numberShowEvent = 0           ! print event record n times

! 3) Beam parameter settings. Values below agree with default ones.
Beams:idA = 2212                   ! first beam, p = 2212, pbar = -2212
Beams:idB = 2212                   ! second beam, p = 2212, pbar = -2212

! 4) Hard process : ttbar pair production at 100TeV
Beams:eCM = 100000.  ! CM energy of collision

ExtraDimensionsG*:all = on
ExtraDimensionsG*:kappaMG = 0.54
5100039:onMode = off
5100039:onIfAny = 23
5100039:m0 = 2000
23:onMode = off
23:onIfAny = 1 2 3 4 5

ParticleDecays:tau0Max = 10        ! ... if c*tau0 > 10 mm
ParticleDecays:limitCylinder = on
ParticleDecays:xyMax = 20          ! mm
ParticleDecays:zMax = 30000        ! mm, (full extent of beampipe)