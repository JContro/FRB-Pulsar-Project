#!/bin/bash

# for loop that changes the directory to each day of data
for dir in `ls -d 20*`; do
# first eneter the mainpulse directory
  cd $dir/mainpulse
# go through all the files in the mainpulse folder 
#  for files in `ls -d *FITS.en`; do
# send all the files to the AllEnFiles.txt
#    cat $files >> /raid1/mm2/crab/AllEnFiles.txt
#  done
# go through the all the files in the mainpulse folder searching for the ASCII files
  ls -1 ${PWD}/*.asc >> /raid1/mm2/crab/AllAscFiles.txt

  cd ../../
done
