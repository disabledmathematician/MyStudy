import math
from time import sleep
import humanize
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
	countPythagorean = 1
	countMersenne = 1
	for n in range(1, 1024):
		q = 4 * n + 1
		qIsPrime = is_prime(q)
		
		if qIsPrime:
			print("4n + 1: {}, Is a prime number: {}, Which prime: {}".format(q, qIsPrime, q))
			print("{} is the {} Pythagorean prime".format(q, humanize.ordinal(countPythagorean)))
			countPythagorean += 1
			sleep(0.3)
		else:
				print("4n + 1: {}, Is a prime number: {}, Which composite: {}".format(q, qIsPrime, q))
				sleep(0.3)
		r = (2 ** n) - 1
		rIsPrime = is_prime(r)
		if rIsPrime:
			print("2 to the n - 1: {}, Is a Mersenne prime {}, Which prime: {}".format(r, rIsPrime, r))
			print("{} is the {} Mersenne prime".format(r, humanize.ordinal(countMersenne)))
			countMersenne += 1
			sleep(0.3)
		else:
			print("2 to the n - 1: {}, Is a Mersenne Prime: {}, Which composite: {}".format(r, rIsPrime, r))
			sleep(0.3)
 			
Charles()