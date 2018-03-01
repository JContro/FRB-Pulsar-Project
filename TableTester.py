# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:06:06 2018

@author: Jack
"""

from astropy.table import Table
import numpy as np

tableT = Table.read('EnFileData.fits')

import matplotlib.pyplot as plt



del_rows = []

for i in range(0,len(tableT['on pulse E'])):
    if tableT['on pulse E'][i] < 0:
       del_rows.append(i) 
tableT.remove_rows(del_rows)


tableT.write('FilteredEnFileData.fits', overwrite = True)

# Create a cumulative distribution
NewNpArray = np.array(tableT['on pulse E'])
NewNpArray = np.log(NewNpArray)
NewNpArray.sort()

NumberEvents = np.arange(len(NewNpArray)) + 1
NumberEvents = np.log(NumberEvents)

plt.plot(NewNpArray, NumberEvents)
plt.xlabel('On Pulse E (log scale) [arbitrary units]')
plt.ylabel('Cumulative distribution (log scale)')
plt.show()


