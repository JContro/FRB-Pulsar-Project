from astropy.table import Table
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

pulsarData = Table.read('FilteredEnFileData.fits')

#Use this area to convert from telescope units to Janskys etc.

NewNpArray = np.array(pulsarData['on pulse E'])


NewNpArray.sort()

NewList = NewNpArray.tolist()
NewList.sort()
print(len(NewList))

NumberEvents = np.arange(len(NewNpArray)) + 1


#function for optimise_curve to fit the data to.
def func2(x, A, c):
	return A*np.power(x, c)

def func(x, A, c):
	return func2(x, A, c)

#Now loop between two cutoff energy ranges, judged by eye from the log log plot.

cutoffE1 = np.linspace(0.07, 0.25, 50) #example range
cutoffE2 = np.linspace(10, 200 , 50) #higher range
#print(cutoffE1)
minError = 0
cutoffs = []
for E1 in cutoffE1:
	
	for E2 in cutoffE2:
		c = 0
		flagLow = False
		flagMid = False
		lowData = []
		lowNum = []
		midData = []
		midNum = []
		highData = []
		highNum = []
		for elem in NewNpArray:
			#print(elem)
			if elem >= E1 and flagLow == False: #first element higher than E1 cutoff
				flagLow = True
				#set up new array
				lowData = NewNpArray[:c-1]
				lowNum = NumberEvents[:c-1]
				lowCut = c-1
			elif elem>=E2 and flagMid == False: #first element higher than E2 cutoff
				flagMid = True
				midData = NewNpArray[lowCut:c-1]
				midNum = NumberEvents[lowCut:c-1]
				highCut = c-1
				highData = NewNpArray[highCut:]
				highNum = NumberEvents[highCut:]
				#print('hi')
				break
			c +=1
	
		#print(lowData)
		#print(midData)
		#print(highData)

		#now have the arrays set up, so do the fittings
		poptLow, pcovLow = curve_fit(func, lowData, lowNum)
		poptMid, pcovMid = curve_fit(func, midData, midNum)
		poptHigh, pcovHigh = curve_fit(func, highData, highNum)
		print(pcovHigh)
		print(pcovMid)
		print(pcovLow)

		lowErr = np.sqrt(np.diag(pcovLow))
		midErr = np.sqrt(np.diag(pcovMid))
		highErr = np.sqrt(np.diag(pcovHigh))

		totalE = np.linalg.norm([lowErr, midErr, highErr])

		#work out if this cuttoffs is an improvement on the error
		if np.isinf(totalE) != True: #not high errors
			print(yay)
			if minError == 0: #first one
				minError = totalE
				cutoffs.append(lowCut)
				cutoffs.append(highCut)
			else: #not first one
				if totalE < minError:
					minError = totalE
					cutoffs[0] = lowCut
					cutoffs[1] = highCut
		else:
			print(totalE)
	print(E1)

print(cutoffs)
print(minError)
#Final arrays with lowest error
lowData = NewNpArray[:cutoffs[0]]
lowNum = NumberEvents[:cutoffs[0]]
midData = NewNpArray[lowCut:cutoffs[1]]
midNum = NumberEvents[lowCut:cutoffs[1]]
highData = NewNpArray[cutoffs[1]:]
highNum = NumberEvents[cutoffs[1]:]

poptLow, pcovLow = curve_fit(func, lowData, lowNum)
poptMid, pcovMid = curve_fit(func, midData, midNum)
poptHigh, pcovHigh = curve_fit(func, highData, highNum)


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



