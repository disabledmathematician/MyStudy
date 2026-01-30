import numpy as np

def ctruscott_CharliersCheck(L, f):
	max_elem = np.where(f == max(f))[0]
	print("L[max_elem] {}".format(L[max_elem]))
	print("Where: {}".format(np.where(f == max(f))[0]))
	print("len(L) - max_elem {}".format(len(L) - max_elem - 1))
	print("minus max_elem: {}".format(-max_elem))
	u_low = np.arange(0, -max_elem - 1, -1)
	u_low = u_low[::-1]
	u_high = np.arange(1, len(L) - max_elem, 1)
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

def CharlesTruscott():
	L = np.array([70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114, 118, 122, 126], dtype="int")
	f = np.array([4, 9, 16, 28, 45, 66, 85, 72, 54, 38, 27, 18, 11, 5, 2], dtype="int")
	ctruscott_CharliersCheck(L, f)
	L = np.array([34.5, 44.5, 54.5, 64.5, 74.5, 84.5, 94.5], dtype="int")
	f = np.array([2, 3, 11, 20, 32, 25, 7], dtype="int")
	ctruscott_CharliersCheck(L, f)

if __name__ == """__main__""": CharlesTruscott()