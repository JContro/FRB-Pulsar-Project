"""
Created on Tue Feb  6 11:48:11 2018

@author: user
"""
from astropy.table import Table
Dtest = []
count = 0
Date = 'Error has occurred'
PulseID = 'Error has occurred'
tableTest = Table(names = ['Pol #', 'Freq #', 'sub int #', 'on pulse peak', 'offpulse peak','on pulse E', 'offpulse E', 'onpulse Rms', 'offpulse RMS' , 'S/N','Date','PulseID'], dtype = ['f','f','f','f','f','f','f','f','f','f','i','i'])
with open('AllEnFiles.txt') as f:
    for line in f:
        charC = 0
        flag = False
        for char in line:
            if charC ==0 and (char.isalpha() == False and char != '#' and char!= '$'):
                #This is the lines with the numerical data on
                flag = True
                break #exit character loop
	    elif char == '$':
		line = line.rstrip()
		DirArr = line.split('/')
		Date = DirArr[4]
		PulseID = DirArr[6]
		PulseID = PulseID.rstrip('.FITS.en')
		if PulseID.startswith('pulse_'):
		  PulseID = PulseID[6:]
		break
            else:
                break #not needed these lines
        if flag == True:#store line
            line = line.rstrip()
            lineArr = line.split(' ')#split into an array with each number input as an item
            c = 0
            for element in lineArr:
                lineArr[c] = float(lineArr[c])
                c+= 1
	    lineArr.append(Date)
	    lineArr.append(PulseID)
            tableTest.add_row(lineArr)
	    count +=1
	    
	    if count%5000 == 0:
		tableTest.write('EnFileData.fits', overwrite = True)
 		print(count)
		print(tableTest)

tableTest.write('EnFileData.fits', overwrite = True)

