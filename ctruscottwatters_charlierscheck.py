""" Charles Truscott Watters

Charlier's Check """

""" 19th of September 2026 """

""" top frequency: 85
 subscript max: 6
 f[subscript max]: 85
 decrease val: -7
 increase val: 9
 uArray: [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

fu: [-24, -45, -64, -84, -90, -66, 0, 72, 108, 114, 108, 90, 66, 35, 16]
Summation of Frequencies: 480
Summation of the product of f and u: 236

sum fu squared: 3404
top frequency: 32
 subscript max: 4
 f[subscript max]: 32
 decrease val: -5
 increase val: 3
 uArray: [-4, -3, -2, -1, 0, 1, 2]

fu: [-8, -9, -22, -20, 0, 25, 14]
Summation of Frequencies: 100
Summation of the product of f and u: -20

sum fu squared: 176

[Program finished]

"""


def CharliersCheck_ctruscottwatters(X, f):
	topFrequency = max(f)
	subscriptMax = 0
	for n in range(len(f)):
		if f[n] == topFrequency:
			subscriptMax = n
	decreaseVal = -subscriptMax - 1
	increaseVal = len(X) - subscriptMax
	descendingArray = [n for n in range(0, decreaseVal, -1)]
	increasingArray = [n for n in range(1, increaseVal)]
	uArray = descendingArray[::-1] + increasingArray
	print("top frequency: {}\n subscript max: {}\n f[subscript max]: {}\n decrease val: {}\n increase val: {}\n uArray: {}\n".format(topFrequency, subscriptMax, f[subscriptMax], decreaseVal, increaseVal, uArray))
	fu = []
	fus = []
	for n in range(len(uArray)):
		fu.append(f[n] * uArray[n])
	print("fu: {}".format(fu))
	for n in range(len(uArray)):
		fus.append(f[n] * uArray[n] ** 2)
	N = sum(f)
	sumFu = sum(fu)
	
	print("Summation of Frequencies: {}\nSummation of the product of f and u: {}\n".format(N, sumFu))
	sumFus = sum(fus)
	print("sum fu squared: {}".format(sumFus))
X = [70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126]
f = [4, 9, 16, 28, 45, 66, 85, 72, 54, 38, 27, 18, 11, 5, 2]
CharliersCheck_ctruscottwatters(X, f)
X = [34.5, 44.5, 54.5, 64.5, 74.5, 84.5, 94.5]
f = [2, 3, 11, 20, 32, 25, 7]
CharliersCheck_ctruscottwatters(X, f)