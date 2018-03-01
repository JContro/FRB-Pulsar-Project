from astropy.table import Table
import numpy as np
col1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
col2 = np.array([2,4,13,124,123,2,3234,23,-123,1,-123,-32,123,14,23])

tableT = Table.read('EnFileData.fits')
del_rows = []
print(tableT)
for i in range(0,len(tableT['on pulse E'])):
    if tableT['on pulse E'][i] < 0:
       del_rows.append(i) 
tableT.remove_rows(del_rows)
print(tableT)

tableT.write('FilteredEnFileData.fits', overwrite = True)

