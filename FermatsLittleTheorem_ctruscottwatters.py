
import math
from time import sleep

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
	for n in range(2, 1024):
		if is_prime(n) == True:
			x.append(n)
	y = []
	x2 = []
	for a in range(2, 33):
		for p in x:
			if ((a ** p)% p) == a:
				y.append(a ** p)
				print("p: {}, a: {}, a ** p: {}  a ** p: {} mod p".format(p, a, a ** p, (a ** p) % p))
				sleep(0.02)
				
if __name__ == """__main__""": Charles()