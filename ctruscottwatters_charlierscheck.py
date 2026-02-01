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
	for n in range(len(uArray)):
		fu.append(f[n] * uArray[n])
	print("fu: {}".format(fu))
	N = sum(f)
	sumFu = sum(fu)
	print("Summation of Frequencies: {}\nSummation of the product of f and u: {}\n".format(N, sumFu))
X = [70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126]
f = [4, 9, 16, 28, 45, 66, 85, 72, 54, 38, 27, 18, 11, 5, 2]
CharliersCheck_ctruscottwatters(X, f)
X = [34.5, 44.5, 54.5, 64.5, 74.5, 84.5, 94.5]
f = [2, 3, 11, 20, 32, 25, 7]
CharliersCheck_ctruscottwatters(X, f)