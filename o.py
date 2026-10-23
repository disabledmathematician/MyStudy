import statistics
import matplotlib.pyplot as plt
from collections import Counter
def Charles():
	L = [1, 2, 3, 3, 2, 6, 4, 3, 6, 1, 8, 1, 1, 10, 10, 2, 2, 6, 4, 6,2, 6]
	C = Counter(L)
	C = dict(C)
	print(C)
	values = []
	freqs = []
	for k in C:
		values.append(k)
		freqs.append(C[k])
	print(f"Values: {values}, Frequencies: {freqs}")
	month_values = []
	for count in range(len(values)):
		if values[count] == 1:
			values[count] = "January"
		elif values[count] == 2:
			values[count] = "February"
		elif values[count] == 3:
			values[count] = "March"
		elif values[count] == 4:
			values[count] = "April"
		elif values[count] == 5:
			values[count] = "May"
		elif values[count] == 6:
			values[count] = "June"
		elif values[count] == 7:
			values[count] = "July"
		elif values[count] == 8:
			values[count] = "August"
		elif values[count] == 9:
			values[count] = "September"
		elif values[count] == 10:
			values[count] = "October"
		elif values[count] == 11:
			values[count] = "November"
		elif values[count] == 12:
			values[count] = "December"
			
	plt.figure(0, dpi=150, figsize=[7, 7])
	plt.title("Charles Truscott. Month of Highest Daily Rain (Byron Bay) 2003 to 2024")
	plt.pie(freqs, labels=values, autopct='%1.1f%%')
	plt.savefig("pie.png")
	print(len(L))
	n = 0
	c = 0
	for e in L:
		if e == 6:
			n += 1
		c += 1
	print(c)
	print(statistics.mode(L))
	print(n)
Charles()