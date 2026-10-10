from math import sqrt
import matplotlib.pyplot as plt
import random
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
	return std
	
def Charles_StdDev_Normal(L: list) -> float:
	std = 0
	mean = Charles_Mean(L)
	for e in L:
		std += (e - mean) ** 2
	std /= len(L)
	std = sqrt(std)
	print(std)
	return std
	
def Charles_NormDib(mean: float, stddev: float):
	pi = 3.14159
	e = 2.71828
	y = []
	x = [n for n in range(-10, 10)]
	plt.figure(0)
	for z in x:
		nd = ((1 / (stddev * sqrt(2 * pi))) * e) ** ((z - mean) ** 2 / ((2 * stddev ** 2)))
		y.append(nd)
	plt.plot(x, y)
	plt.show()
	
def Charles():
#	L = [2, 4, 8, 1]
	L = []
	for n in range(-30, 30):
		L.append(n)
	stddev = Charles_StdDev_SquareMean(L)
	mean = Charles_Mean(L)
	Charles_StdDev_Normal(L)
	Charles_NormDib(0, 2.14)
Charles()