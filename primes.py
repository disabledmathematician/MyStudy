import math
from time import sleep
import humanize
import sys
sys.set_int_max_str_digits(1000000)
""" Charles Thomas Wallace Truscott. Verifying primes in a log2(n) computational complexity.

I love you Dad Mark William Watters, big brother Tai

127 Broken Head Rd Suffolk Park NSW 2481

A use case of Bisection Search to identify primes. a log2(n) greedy algorithm

"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    factors = [x for x in range(2, n)]
    low = 0
    high = len(factors) - 1
    while low <= high:
    	mid = (high + low) // 2
    	print("Factor tried: {} Index: {}".format(factors[mid], mid))
    	if n % factors[mid] == 0:
    		return False
    	if factors[mid] < n:
    		low = mid + 1
    	else:
    		high = mid - 1
    		
    return True
 
def Charles():
	txt = open("FermatNums.txt", "w+")
	countFermat = 1
	for n in range(0, 7):
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

"""
Factor tried: 2 Index: 0
2 to the 2 to the n + 1: 3, Is a Fermat prime True, Which prime: 3

3 is the 1st Fermat prime
Factor tried: 3 Index: 1
Factor tried: 4 Index: 2
2 to the 2 to the n + 1: 5, Is a Fermat prime True, Which prime: 5

5 is the 2nd Fermat prime
Factor tried: 9 Index: 7
Factor tried: 13 Index: 11
Factor tried: 15 Index: 13
Factor tried: 16 Index: 14
2 to the 2 to the n + 1: 17, Is a Fermat prime True, Which prime: 17

17 is the 3rd Fermat prime
Factor tried: 129 Index: 127
Factor tried: 193 Index: 191
Factor tried: 225 Index: 223
Factor tried: 241 Index: 239
Factor tried: 249 Index: 247
Factor tried: 253 Index: 251
Factor tried: 255 Index: 253
Factor tried: 256 Index: 254
2 to the 2 to the n + 1: 257, Is a Fermat prime True, Which prime: 257

257 is the 4th Fermat prime
Factor tried: 32769 Index: 32767
Factor tried: 49153 Index: 49151
Factor tried: 57345 Index: 57343
Factor tried: 61441 Index: 61439
Factor tried: 63489 Index: 63487
Factor tried: 64513 Index: 64511
Factor tried: 65025 Index: 65023
Factor tried: 65281 Index: 65279
Factor tried: 65409 Index: 65407
Factor tried: 65473 Index: 65471
Factor tried: 65505 Index: 65503
Factor tried: 65521 Index: 65519
Factor tried: 65529 Index: 65527
Factor tried: 65533 Index: 65531
Factor tried: 65535 Index: 65533
Factor tried: 65536 Index: 65534
2 to the 2 to the n + 1: 65537, Is a Fermat prime True, Which prime: 65537

65537 is the 5th Fermat prime
"""
