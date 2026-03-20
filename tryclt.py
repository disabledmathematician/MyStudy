import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as ss
import math
import statistics
import seaborn as sns
def Charles():
	random.seed(0)
	samples = []
	population = []
	for p in range(0, 10000):
		population.append(random.randint(0, 999))
	for p in range(0, 1000):
		choices = []
		for q in range(0, 30):
			choices.append(random.choice(population))
		samples.append(choices)
	print(samples)
	sample_means = []
	for l in samples:
		sample_means.append(statistics.mean(l))
	print(sample_means)
	sns.histplot(sample_means, kde=True)
#	plt.title("Distribution of Sample Means (n=50)")
	plt.xlabel("Sample Mean")
	plt.show()
#	plt.title("Implementing the CLT")
#	plt.hist(sample_means)
	plt.show()
Charles()