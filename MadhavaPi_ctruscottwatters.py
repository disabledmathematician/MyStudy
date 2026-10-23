import math
def Madhava():
	
	""" Charles Truscott Watters
	3.141592653589794

[Program finished] """

	i = 1
	o = []
	exponent = 1
	for n in range(1, 1000):
		if n % 2 == 1:
			o.append(n)
	for n in range(1, len(o)):
		if n % 2 == 1:
			i -= 1 / (o[n] * 3 ** exponent)
			exponent += 1
#			print("n is odd and we are subtracting: {}".format(n % 2 == 1))
#			print("Subtracting 1 / n: {}".format(1 / o[n]))
		elif n % 2 == 0:
			i += 1 / (o[n] * 3 ** exponent)
			exponent += 1
#			print("n is even and we are adding: {}".format(n % 2 == 0))
#			print("Adding 1 / n: {}".format(1 / o[n]))
#		print("n: {}, o[n]: {}".format(n, o[n]))
	print(i * math.sqrt(12))
Madhava()