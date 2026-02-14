import math
from time import sleep
import humanize
import sys
sys.set_int_max_str_digits(1000000)
""" Charles Thomas Wallace Truscott. Verifying primes in a log2(n) computational complexity.

I love you Dad Mark William Watters, big brother Tai

127 Broken Head Rd Suffolk Park NSW 2481

A use case of Bisection Search to indentify primes. a log2(n) greedy algorithm

"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    low = 0
    high = n
    guess = (high + low) / 2.0
    while n % guess != 0:
    	if guess ** 2 > n:
    		high = guess
    		if n % guess == 0:
    			return False
    	elif guess ** 2 < n:
    	 	low = guess
    	 	if n % guess == 0:
    	 		return False
    	guess = (high + low) / 2.0
    return True
 
def Charles():
	txt = open("FermatNums.txt", "w+")
	countFermat = 1
	for n in range(0, 20):
		s = (2 ** 2 ** n) + 1
		sIsPrime = is_prime(s)
		if sIsPrime:
			print("2 to the 2 to the n + 1: {}, Is a Fermat prime {}, Which prime: {}\n".format(s, sIsPrime, s))
			txt.write("2 to the 2 to the n + 1: {}, Is a Fermat prime {}, Which prime: {}\n".format(s, sIsPrime, s))
			print("{} is the {} Fermat prime".format(s, humanize.ordinal(countFermat)))
			txt.write("{} is the {} Fermat prime\n".format(s, humanize.ordinal(countFermat)))
			countFermat += 1
		else:
			print("2 to the 2 to the n + 1: {}, Is a Fermat Prime: {}, Which composite: {}\n".format(s, sIsPrime, s))
			txt.write("2 to the 2 to the n + 1: {}, Is a Fermat Prime: {}, Which composite: {}\n".format(s, sIsPrime, s))
	txt.close()
Charles()
