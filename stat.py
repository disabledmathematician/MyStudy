from math import sqrt

def Charles_Mean(L: list):
	n = 0
	for e in L:
		n += e
	n /= len(L)
	return n

def Charles_StdDev_SquareMean(L: list) -> float:
	squared_vals = []
	for e in L:
		squared_vals.append(e ** 2)
	square_mean = Charles_Mean(squared_vals)
	regular_mean = Charles_Mean(L)
#	print(square_mean)
#	print(regular_mean)
	std = sqrt((square_mean - (regular_mean ** 2)))
	print(std)
	pass
	
def Charles_StdDev_Normal(L: list) -> float:
	std = 0
	mean = Charles_Mean(L)
	for e in L:
		std += (e - mean) ** 2
	std /= len(L)
	std = sqrt(std)
	print(std)
	return std
	
def Charles():
	L = [2, 4, 8, 1]
	Charles_StdDev_SquareMean(L)
	Charles_StdDev_Normal(L)
Charles()