from astropy.table import Table
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn import preprocessing

pulsarData = Table.read('FilteredEnFileData.fits')
NewNpArray = np.array(pulsarData['on pulse E'])
NewNpArray.sort()

NumberEvents = np.arange(len(NewNpArray)) + 1

logDat = np.log(NewNpArray)
logNum = np.log(NumberEvents)

def func(x, a1, c1, xlow, a2, c2, xup, a3, c3):
	y = []
	for xx in x:
		if(x.all()<xlow):
			y.append(a1*xx + c1)
		elif(x.all()>xlow and x.all()<xup):
			y.append((a2*xx + c2))
		elif(x.all()>xup):
			y.append((a3*xx + c3))
	return y



#def func2(x, A, xlow, d, B, xup, e ,C, f, Z):
	#return np.log(A*np.power(x-xlow,d) + B*np.power(x-xup, e) + C*np.power(x, f) + Z)
guess = [1, 8, -2, 1.2, 5.3, 3.8, 0.1, 12]
popt, pcov = curve_fit(func, logDat, logNum, guess)

print(popt)
print(np.sqrt(np.diag(pcov)))
plt.figure(1)
plt.plot(logDat, logNum, 'r-x', label = 'pulse data')
plt.plot(logDat, func(logDat, *popt), 'g--', label = 'curve fit')
plt.show()
