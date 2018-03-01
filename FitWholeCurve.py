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

def func(x, A, xlow, d, B, xup, e, C, f, Z):
	return A*np.power(x-xlow,d) + B*np.power(x-xup, e) + C*np.power(x, f) + Z


low = []
lowNum = []
mid = []
midNum = []
high = []
highNum = []
guessL = [0.5, 9]
guessM = [3.75 ,6]
guessH = [0, 12.3]
boundsL = [[0.1, 7], [2, 11]]
boundsM = [[0.5,2 ],[5,7]]
boundsH = [[0, 12], [0.5, 13.5]]
c=0
for elem in logDat:
	if elem < -2: #low
		low.append(elem)
		lowNum.append(logNum[c])
	elif elem >= -2 and elem < 3.8:
		mid.append(elem)
		midNum.append(logNum[c])
	elif elem >= 3.8:
		high.append(elem)
		highNum.append(logNum[c])
	c += 1

#def func2(x, A, xlow, d, B, xup, e ,C, f, Z):
	#return np.log(A*np.power(x-xlow,d) + B*np.power(x-xup, e) + C*np.power(x, f) + Z)
#guess = [1, 2, 1, 0.8, 1, -2]
poptL, pcovL = curve_fit(fnLow, low, lowNum, p0 = guessL, bounds = ((0.1,0),(5,11)))
poptM, pcovM = curve_fit(fnMid, mid, midNum, p0 = guessM, bounds = ((0.5,2 ),(5,7)))
poptH, pcovH = curve_fit(fnHigh, high, highNum, p0 = guessH, bounds = ((0, 12), (0.5, 13.5)))
#popt2, pcov2 = curve_fit(func, scaledE, scaledNum)

print(np.sqrt(np.diag(pcovL)))
print(np.sqrt(np.diag(pcovM)))
print(np.sqrt(np.diag(pcovH)))
print(len(low))
yLow = []
c=0
#for elem in low:
#	yLow.append(fnLow(low[c], poptL[0], poptL[1]))
#	c += 1
print(poptL)
print(poptM)
print(poptH)

plt.figure(1)
plt.plot(logDat, logNum, 'r-x')

#plt.plot(NewNpArray, NumberEvents, 'r-x', label = 'pulse data')
#plt.plot(NewNpArray, func(NewNpArray, *popt), 'g--', label = 'curve fit')
#plt.title('regular axes')
#plt.legend(loc = 2)


midps = [np.zeros(len(mid)), np.zeros(len(mid))]
midps[0][:] = poptM[0]
midps[1][:] = poptM[1]
highps = [np.zeros(len(high)), np.zeros(len(high))]
highps [0][:] = poptH[0]
highps[1][:] = poptH[1]

plt.figure(2)
plt.plot(logDat, logNum, 'r-x', label = 'pulse data')
plt.plot(low, fnLow(low, *poptL), 'g--', label = 'curve fit')
plt.plot(mid, fnMid(mid, *poptM), 'g--', label = 'curve fit')
plt.plot(high, fnHigh(high, *poptH), 'b--', label = 'curve fit')


#plt.legend(loc = 2)
#plt.figure(3)
#plt.plot(scaledE, scaledNum, 'r-x')
#plt.plot(scaledE, func(scaledE, *popt2), 'g--', label = 'curve fit')

#plt.figure(4)
#plt.loglog(scaledE, scaledNum, 'r-x')
#plt.loglog(scaledE, func(scaledE, *popt2), 'g--', label = 'curve fit')
plt.show()


