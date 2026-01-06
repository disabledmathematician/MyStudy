import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def is_prime(n):
    """Check if an integer n is a prime number."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True
 
def Charles():
	plt.figure(dpi=120, figsize=[12, 7])
	x = []
	for n in range(0, 1024):
		if is_prime(n) == True:
			x.append(n)
	y = []
	x2 = []
	for n in range(len(x)):
		for e in x:
			y.append(e ** n)
			print("e: {}, n: {}, n ** e: {}".format(e, n, n ** e))
#	print(x)
#	print(len(y))
	print(y)
if __name__ == """__main__""": Charles()