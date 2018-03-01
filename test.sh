#!/bin/bash

for dir in `ls -d 20*`; do
  cd $dir/mainpulse
  for files in `ls -d *FITS.en`; do
    echo "\$$PWD/$files" >> /raid1/mm2/crab/AllEnFiles.txt
    cat $files >> /raid1/mm2/crab/AllEnFiles.txt
  done
  cd ../../
done
