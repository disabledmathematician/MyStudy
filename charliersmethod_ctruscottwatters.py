
import numpy as np
from math import floor, ceil
import statistics
def ctruscott_CharliersCheck():
	L = np.array([70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126], dtype="float")
	if len(L) % 2 == 0:
		m1 = (len(L) / 2) + 1
		m2 = (len(L) / 2)
		midpoint = L[floor((m1 + m2) / 2)]
		midpoint_index = floor((m1 + m2) / 2)
		print("Even length, midpoints {}, {}".format(m1, m2))
	else:
		m3 = len(L) // 2
		midpoint_index = floor(m3)
		midpoint = L[m3 - 1]
		print("Odd length, midpoints {}".format(m3))
	f = np.array([4, 9, 16, 28, 45, 66, 85, 72, 54, 38, 27, 18, 11, 5, 2])
	print("L: {}, midpoint: {}".format(L, midpoint))
#	roots = np.sqrt(L)
#	u = (L - midpoint) / f
	print("L - midpoint: {}".format(L - midpoint))
	lower = np.arange(0, - midpoint_index, -1, dtype="float")
	print(midpoint_index)
	upper = np.arange(1, midpoint_index + 1 + 1, 1, dtype="float")
	print("upper: {}, lower: {}".format(upper, lower))
	lo = lower[::-1]
	uo = upper
	u = np.concatenate((lo, uo))
	print("u: {}, \n f: {}".format(u, f))
	print("f * u: {}".format(u * f))
	print("fu squared: {}".format((f * (u ** 2))))
	uplusone = u + 1
	print("u + 1: {}".format(uplusone))
	ufsquared = uplusone * f * uplusone
	print("f(u + 1) ** 2: {}, Sum of f(u + 1) ** 2: {}".format(ufsquared, ufsquared.sum()))
	fsum = f.sum()
	ufsum = (u * f).sum()
	print("f sum: {}, uf sum: {}".format(fsum, ufsum))
	print("f sum plus uf sum: {}".format(fsum + ufsum))
	fuplusone = f * uplusone
	fuplusonesum = fuplusone.sum()
	print("f(u + 1) sum: {}".format(fuplusonesum))
	print("f(u+1) sum is equal to f sum plus uf sum: {}".format((fsum + ufsum) == fuplusonesum))
#	fuplusone= ((f) * (u + 1))
#	print("f(u + 1): {}".format(fuplusone))
#	fuplusonesum = fuplusone.sum()
#	print("Sum of f(u + 1): {}".format(fuplusonesum))
#	fuplusonesquard = fuplusone ** 2
#	print("f(u + 1) ** 2: {}".format(fuplusone ** 2))
#	fuplusonesumsquared = (fuplusone ** 2).sum()
#	print("Sum of f(u + 1) **2: {}".format(fuplusonesumsquared))
ctruscott_CharliersCheck()