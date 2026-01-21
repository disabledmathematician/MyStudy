import numpy as np
from math import floor, ceil
import statistics
def ctruscott_CharliersCheck():
	L = np.array([70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126], dtype="float")
	f = np.array([4, 9, 16, 28, 45, 66, 85, 72, 54, 38, 27, 18, 11, 5, 2], dtype="float")
	midpoint = np.median(L)
	u_low = np.arange(0, -(len(L))// 2 + 1, -1)
	u_low = u_low[::-1]
	u_high = np.arange(1, (len(L) // 2) + 2, 1)
#	print(u_low)
#	print(u_high)
	u = np.concatenate((u_low, u_high))
#	print(f, u, len(f), len(u))
	fu = f * u
	print(f)
	print(fu)
	sum_f = f.sum()
	sum_fu = fu.sum()
	print(sum_f, sum_fu)
	uplusone = u + 1
	uplusonesquared = u * u
	fuplusone = f * uplusone
	print(sum_f + sum_fu)
	print(fuplusone.sum())
ctruscott_CharliersCheck()
	