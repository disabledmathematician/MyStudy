import math

def Charles():
	Odds = []
	for n in range(1, 3000000):
		if n % 2 == 0:
			continue
		else:
			Odds.append(n)
	print(Odds)
	Reciprocals = []
	for n in Odds:
		Reciprocals.append(1/n)
	print(Reciprocals)
	n = 1
	for e in range(1, len(Reciprocals)):
		print("e: {}, Reciprocals[e] : {}, n: {}".format(e, Reciprocals[e], n))
		if e % 2 == 0:
			n += Reciprocals[e]
			print("Adding {} to {}".format(Reciprocals[e], n))
		elif n % 2 != 0:
			n -= Reciprocals[e]
			print("Subtracting {} from {}".format(Reciprocals[e], n))
	print(n * 4)
	print(math.pi)
	print(round(n * 4, 4), round(math.pi, 4))
	print(round(n * 4, 5) == round(math.pi, 5))
Charles()