
import math


"""


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
	x = []
	for n in range(0, 1024):
		if is_prime(n) == True:
			x.append(n)
	y = []
	x2 = []
	for n in range(len(x)):
		for e in x:
			y.append(n ** e)
			print("e: {}, n: {}, n ** e: {} mod e".format(e, n,(n ** e) % e))
#	print(x)
#	print(len(y))
#	print(y)
if __name__ == """__main__""": Charles()