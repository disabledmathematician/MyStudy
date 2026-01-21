import numpy as np
from math import floor, ceil
import statistics
def ctruscott_CharliersCheck():

	
#	L = np.array([70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126], dtype="int")
#	f = np.array([4, 9, 16, 28, 45, 66, 85, 72, 54, 38, 27, 18, 11, 5, 2], dtype="int")
#	
	L = np.array([34.5, 44.5, 54.5, 64.5, 74.5, 84.5, 94.5], dtype="int")
	f = np.array([2, 3, 11, 20, 32, 25, 7], dtype="int")
	
	midpoint = np.median(L)
	u_low = np.arange(0, -(len(L))// 2 - 1, -1)
	u_low = u_low[::-1]
	u_high = np.arange(1, (len(L) // 2), 1)
	print("u low {} u high {}".format(u_low, u_high))
	print("f: {}".format(f))
	print("Sum of f: {}".format(f.sum()))
	
#	print(u_low)
#	print(u_high)
	u = np.concatenate((u_low, u_high))
#	print(f, u, len(f), len(u))
#	print("u high: {}".format(u_high))
	fu = f * u
	print("f u: {}".format(fu))
	print("Sum of fu: {}".format(fu.sum()))
	sum_f = f.sum()
	sum_fu = fu.sum()
	usquared = u * u
	fusquared = f * usquared
	print("fu squared: {}".format(fusquared))
	print("Sum of fu squared: {}".format(fusquared.sum()))
	fusquaredsum = fusquared.sum()
	uplusone = u + 1
	uplusonesquared = uplusone * uplusone
	fuplusone = f * uplusone
	fuplusonesquared = f * uplusonesquared
	print("f(u + 1) squared: {}".format(fuplusonesquared))
	print("Sum of f(u + 1) squared: {}".format(fuplusonesquared.sum()))
	print(sum_f + sum_fu)
	print(fuplusone.sum())
	variance = fusquaredsum / sum_f - ((fu.sum() / sum_f) ** 2)
	print(variance)
"""
'u low [-4 -3 -2 -1  0] u high [1 2]
f: [ 2  3 11 20 32 25  7]
Sum of f: 100
f u: [ -8  -9 -22 -20   0  25  14]
Sum of fu: -20
fu squared: [32 27 44 20  0 25 28]
Sum of fu squared: 176
f(u + 1) squared: [ 18  12  11   0  32 100  63]
Sum of f(u + 1) squared: 236
80
80
1.72

[Program finished]

"""'
ctruscott_CharliersCheck()
	