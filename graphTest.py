from astropy.table import Table
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


pulsarData = Table.read('FilteredEnFileData.fits')
NewNpArray = np.array(pulsarData['on pulse E'])
NewNpArray.sort()

NumberEvents = np.arange(len(NewNpArray)) + 1

cutoffs = [275, 58627]

lowData = NewNpArray[:cutoffs[0]]
lowNum = NumberEvents[:cutoffs[0]]
midData = NewNpArray[cutoffs[0]:cutoffs[1]]
midNum = NumberEvents[cutoffs[0]:cutoffs[1]]
highData = NewNpArray[cutoffs[1]:]
highNum = NumberEvents[cutoffs[1]:]

def func2(x, A, c):
	return A*np.power(x, c)


poptLow, pcovLow = curve_fit(func2, lowData, lowNum)
poptMid, pcovMid = curve_fit(func2, midData, midNum)
poptHigh, pcovHigh = curve_fit(func2, highData, highNum)

lowErr = np.sqrt(np.diag(pcovLow))
midErr = np.sqrt(np.diag(pcovMid))
highErr = np.sqrt(np.diag(pcovHigh))

totalE = np.linalg.norm([lowErr, midErr, highErr])
print(lowErr)
print(midErr)
print(highErr)
print(totalE)


plt.figure(1)
plt.plot(lowData, lowNum, 'r-x', label = 'pulse data')
plt.plot(lowData, func2(lowData, *poptLow), 'g--', label = 'curve fit')
plt.title('regular axes for lower branch')
plt.legend(loc = 2)

plt.figure(2)
plt.loglog(lowData, lowNum, 'r-x', label = 'pulse data')
plt.loglog(lowData, func2(lowData, *poptLow), 'g--', label = 'curve fit')
plt.title('log log axes for lower branch')
plt.legend(loc = 2)

plt.figure(3)
plt.plot(midData, midNum, 'r-x', label = 'pulse data')
plt.plot(midData, func2(midData, *poptMid), 'g--', label = 'curve fit')
plt.title('regular axes for middle branch')
plt.legend(loc = 2)

plt.figure(4)
plt.loglog(midData, midNum, 'r-x', label = 'pulse data')
plt.loglog(midData, func2(midData, *poptMid), 'g--', label = 'curve fit')
plt.title('log log axes for middle branch')
plt.legend(loc = 2)

plt.figure(5)
plt.plot(highData, highNum, 'r-x', label = 'pulse data')
plt.plot(highData, func2(highData, *poptHigh), 'g--', label = 'curve fit')
plt.title('regular axes for upper branch')
plt.legend(loc = 2)

plt.figure(6)
plt.loglog(highData, highNum, 'r-x', label = 'pulse data')
plt.loglog(highData, func2(highData, *poptHigh), 'g--', label = 'curve fit')
plt.title('log log axes for upper branch')
plt.legend(loc = 2)

plt.show()
