# Script that analysises and shifts the phase of the pulses
from astropy.table import Table

# import the tables
PhaseTable = Table.read('PhaseTable.fits')
ShiftTable = Table.read('PulseShiftTable.fits')

# Correct the phase shifts from 0-1 to 0-1024 (which is the number of bins)
ShiftTable['Phase Shift'] = ShiftTable['Phase Shift']*1024
ShiftTable['Phase Shift Error'] = ShiftTable['Phase Shift Error']*1024

# Create a new astropy table with the new values - for now just copy Phase Table
PhaseCorrTable = PhaseTable

# Create a function that finds the date in the ShiftTable and returns the row number
def ShiftFinder(date):
	date = int(date)
	c=0
	row = 0
	for i in ShiftTable['Date']:	# For each row in the col Date
		i = int(i)
		if i == date:
			row = c
			break
		c += 1
	return(row)

count = 1
# for each row in the PhaseTable change the Phase
for i in PhaseTable['Date']:
	# printing i is ugly
	row = ShiftFinder(i)
	PhaseCorrTable['Phase'][count] = PhaseCorrTable['Phase'][count]+ShiftTable['Phase Shift'][row]
	count += 1
	if count%1000 == 0:
		print(PhaseCorrTable['Phase'][count])
		print(count)