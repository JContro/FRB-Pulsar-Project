"""
Created on Tue Feb  6 11:48:11 2018

@author: user
"""
from astropy.table import Table
import numpy as np
import pandas as pd
DirArr = []
PulseID = 'something went wrong' # it will be obvious if it's not working correctly
count = 0
tableTest = Table(names = ['Date','Pulse ID', 'Phase', 'Intensity'], dtype = ['U10','U10','f','f'])
SaveTable = Table(names = ['Date','Pulse ID', 'Phase', 'Intensity'], dtype = ['U10','U10','f','f'])
count = 0
with open('AllAscFiles.txt') as f: 
    for lineDir in f:
	lineDir = lineDir.rstrip()
	
	print(lineDir) 		# Check the line directory
	tableTest = Table()
	tableTest = Table(names = ['Date','Pulse ID', 'Phase', 'Intensity'], dtype = ['U10','U10','f','f'])	# remake the astropy table - for memory managment		 
        with open(lineDir) as ASC:
	  for line in ASC:
	    lineArr = []
	    charC = 0
	    flag = False
	    for char in line:
	      if charC ==0 and (char.isalpha() == False and char != '#'):
	    	#This is the lines with the numerical data on
       	         flag = True
		
	         break #exit character loop
      	      else:
		 break 
	    if flag == True: # store line
	       
	       line = line.rstrip()
   	       lineArr = line.split(' ') # split into an array with each number input as an item
	       c = 0
	       for element in lineArr:
                 lineArr[c] = float(lineArr[c])
               
	         c+= 1
	       DirArr = lineDir.split('/')
	       
               NewRow = [DirArr[4],str(PulseID),lineArr[2],lineArr[3]]
	     
	       tableTest.add_row(NewRow)
	           # want only the last two columns to add in the astropy table
	    else:
		line = line.rstrip()
		lineArr = line.split(' ')
		PulseID = lineArr[1]
		PulseID = PulseID.rstrip('.FTp8.asc')
		if PulseID.startswith('pulse_'):
		  PulseID = PulseID[6:]
		
	    
	   
	    
	  	# print once all the table is complete
	  tableTest.write('NewTestfile.fits', overwrite = True)
 	  dic = {'Date':tableTest['Date'],'Pulse ID':tableTest['Pulse ID'], 'Phase':tableTest['Phase'], 'Intensity':tableTest['Intensity']}
	  df = pd.DataFrame(data=dic)
	  index = df['Intensity'].argmax()
 	  row = df.T[index] 
	  AstroRow = [row['Date'],row['Pulse ID'],row['Phase'],row['Intensity']]
	  SaveTable.add_row(AstroRow)
	  
	  count += 1
	  
	  if count % 10 == 0:
		print('now here')
		print(count)
		print(SaveTable)
		SaveTable.write('PhaseTable.fits',overwrite = True)
 
SaveTable.write('PhaseTable.fits',overwrite = True)
	  	

    
