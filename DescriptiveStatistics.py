import numpy as np

from Packages import *

random_array = [i for i in random.sample(range(1500), 1000)]

print("Descriptive Statistics:")
print(f"Mean Average: {np.mean(random_array):.2f}")
print(f"Median Average: {np.median(random_array):.2f}")
print(f"Min: {np.min(random_array):.2f}")
print(f"Max: {np.max(random_array):.2f}")
print(f"Count: {len(random_array):.2f}")
print(f"Variance: {np.var(random_array):.2f}")
print(f"Standard Deviation: {np.std(random_array):.2f}")
print(f"25th Percentile: {np.percentile(random_array, 25):.2f}")
print(f"75th Percentile: {np.percentile(random_array, 75):.2f}")
print(f"1.5IQR: {1.5 * np.percentile(random_array, 75) - np.percentile(random_array, 25):.2f}")