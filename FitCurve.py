from astropy.table import Table
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import quad

pulsarData = Table.read('FilteredEnFileData.fits')

#Use this area to convert from telescope units to Janskys etc.




#Plot histograms, cumulative frequencies.
pulsarData['zerod energy'] =(pulsarData['on pulse E'] - pulsarData['offpulse RMS'])

# Create a cumulative distribution
NewNpArray = np.array(pulsarData['on pulse E'])


NewNpArray.sort()

NewList = NewNpArray.tolist()
NewList.sort()
print(len(NewList))

NumberEvents = np.arange(len(NewNpArray)) + 1

plt.figure(1)
plt.plot(NewNpArray, NumberEvents, 'ro') #Cumulative plot


plt.figure(2)
plt.loglog(NewNpArray, NumberEvents, 'ro') #Log Log cumulative plot



#def func(x, lam): #function for the poisson distribution cumulitive distribution function
	#integrand = (np.exp(-lam)*pow(lam,x))/math.factorial(x)
	#return quad(integrand, 0, x)[0] #0 is the integral value
def func(x, c):#logged power law
	return c*np.log(x)
def func2(x, A, c):
	return A*np.power(x, c)

test = np.log(NewNpArray)
print(np.argwhere(np.isnan(test)))


popt, pcov = curve_fit(func2, NewList, NumberEvents, maxfev = len(NewList)) #fit a curve to the specified function
	#popt is the optimal parameter values (value for lamda)
	#pcov is estimated covariance matrix for popt - use to get errors.

print(popt)

plt.figure(3)
plt.plot(NewNpArray, NumberEvents, 'r-x', label = 'pulse data')
plt.plot(NewNpArray, func2(NewNpArray, *popt), 'g--', label = 'curve fit')
plt.title('regular axes')
plt.legend()

plt.figure(4)
plt.loglog(NewNpArray, NumberEvents, 'r-x', label = 'pulse data')
plt.loglog(NewNpArray, func2(NewNpArray, *popt), 'g--', label = 'curve fit')
plt.title('log log axes')
plt.legend()


#print(np.where(np.isnan(np.log(NewList))))
print(NewList[0])
#popt, pcov = curve_fit(func, np.log(NewList), np.log(NumberEvents), maxfev = len(NewList)) #fit a curve to the specified function

testcut = 1020

flag = False
c = 0
for elem in NewNpArray:
	if elem > testcut and flag == False:
		flag = True
		break
	c +=1

EarrCut = NewList[c:]
numCut = NumberEvents[c:]
print(c)

plt.figure(5)
plt.plot(EarrCut, numCut)

popt, pcov = curve_fit(func2, EarrCut, numCut)
print(pcov)

plt.figure(6)
plt.plot(EarrCut, numCut, 'r-x', label = 'pulse data')
plt.plot(EarrCut, func2(EarrCut, *popt), 'g--', label = 'curve fit')
plt.title('regular axes')
plt.legend()

plt.figure(7)
plt.loglog(EarrCut, numCut, 'r-x', label = 'pulse data')
plt.loglog(EarrCut, func2(EarrCut, *popt), 'g--', label = 'curve fit')
plt.title('log log axes')
plt.legend()



plt.show()


#plt.figure(3)
#plt.plot(NewNpArray, NumberEvents, 'ro') #Cumulative plot





