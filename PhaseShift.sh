#!/bin/bash

# First day is 20120511
cd /raid1/mm2/crab/20120511/mainpulse
psradd -o average.ar *.FTp8 
pam -e FTp -FTp average.ar
cd ../../
# return to the crab folder 
rm /raid1/mm2/crab/PhaseShiftOutput.txt # overwrite the file (but will it?)
for direc in `ls -d 20*`; do
  cd $direc/mainpulse
  #in the correct directory -> create the average.ar file for it and the FTp file
 
  psradd -o average.ar *.FTp8
 
  pam -e FTp -FTp average.ar
 
  # for each file FTp file in the mainpulse of each day -> print off to a file the output with a day name (the directory) 
  cd /raid1/mm2/crab/20120511/mainpulse
  # send the output of this command to the PhaseShiftOutput.txt file
  echo `pat -R -s average.FTp ../../$direc/mainpulse/average.FTp` >> /raid1/mm2/crab/PhaseShiftOutput.txt 
  # send the directory of the files so that the values can be saved correctly 
  echo "\$$direc" >> /raid1/mm2/crab/PhaseShiftOutput.txt 
  cd ../../
 
done 

