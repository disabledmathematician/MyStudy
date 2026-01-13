import math
from time import sleep
def is_prime(n):
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
	for n in range(1, 1024):
		q = 4 * n + 1
		IsPrime = is_prime(q)
		if IsPrime:
			print("4n + 1: {}, Is a prime number: {}, Which prime: {}".format(q, IsPrime, q))
			sleep(0.3)
		else:
				print("4n + 1: {}, Is a prime number: {}, Which composite: {}".format(q, IsPrime, q))
				sleep(0.3)
 			
Charles()