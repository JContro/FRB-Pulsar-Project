from astropy.table import Table

# import the two tables, the first one with all hte phases and intensities of the pulses, the second with the day phase shift
PhaseTable = Table.read('PhaseTable.fits')
ShiftTable = Table.read('PulseShiftTable.fits')

# change the phase shift in bins (1-1024) in the ShiftTable
ShiftTable['Phase Shift'] = ShiftTable['Phase Shift']*1024

Phases = PhaseTable['Phase']
Shifts = ShiftTable['Phase Shift']
# get key from the ShiftTable and apply it to the values in the PhaseTable
c2 = 0 
print(Phases)
for i in ShiftTable['Date']:
	
	c1 = 0
	for j in PhaseTable['Date']:
		if j == i:
			Phases[c1] = Phases[c1] + Shifts[c2]
			c1 += 1
			
	c2 += 1
	print(Phases)

