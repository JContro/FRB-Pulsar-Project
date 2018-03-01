from astropy.table import Table

PulseShiftTable = Table(names = ['Date','Phase Shift', 'Phase Shift Error'], dtype = ['U10','f','f'])
with open('PhaseShiftOutput.txt') as f:
	for line in f:
		lineArr = []
		for c in line:
			if c == '.': 
				# read that line and do stuff
				lineArr = line.split(' ')
				DayVar = lineArr[0]
				DayVar = DayVar[6:]
				DayVar = DayVar.rstrip('/mainpulse/average.FTp')
				NewRow = [str(DayVar),lineArr[3],lineArr[4]]
				PulseShiftTable.add_row(NewRow)
				
				break
			else:
				
				break

PulseShiftTable.write('PulseShiftTable.fits',overwrite = True)
