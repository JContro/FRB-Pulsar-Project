#!/bin/bash

for dir in `ls -d 20*`; do
  cd $dir/mainpulse
  for files in `ls -d *FITS.en`; do
    echo $files
  done
  cd ../../
  pwd
done
