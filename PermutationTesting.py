# Script for permutation testing
import random

import matplotlib.pyplot as plt

from Packages import *

Data = {
    "A": [random.choice([0,1]) for i in range(15000)], # assuming this is the holdout set
    "B": [random.choice([0,1]) for i in range(10000)] # assuming this is the test set
}

holdout_array = np.array(Data["A"])
test_array = np.array(Data["B"])

ObsMeanDiff = np.mean(test_array) - np.mean(holdout_array)
print(f"ObsMeanDiff: {ObsMeanDiff:.4f}")

def permutation_function(holout, test, n_perms, direction):

    # Data combinations
    combinedarrays = np.concatenate((holout, test))

    # Lengths of holdout Array
    nHoldout = len(holout)

    # Storing the permutations
    perm_differences = []

    # Loop to get the mean differences
    for i in range(n_perms):
        np.random.shuffle(combinedarrays)
        perm_holdout = combinedarrays[:nHoldout]
        perm_test = combinedarrays[nHoldout:]
        perm_diff = np.mean(perm_test) - np.mean(perm_holdout)
        perm_differences.append(perm_diff)

    PermCountsTwoSided = np.sum(np.abs(perm_differences) >= np.abs(ObsMeanDiff))
    PermCountsOneSided = np.sum(perm_differences >= ObsMeanDiff)
    TwoSidedPvalue = (PermCountsTwoSided / n_perms) # Two sided Pvalue
    OnesidedPvalue = (PermCountsOneSided / n_perms) # One sided Pvalue

    # Setting a boolean to make sure I select either the hist distribution or onesided, twosided or both pvalues.
    if direction == 'both':
        finalarray = [f"Onesided Pvalue: {OnesidedPvalue:.4f}", f"Twosided Pvalue: {TwoSidedPvalue:.4f}"]
    elif direction == 'onesided':
        finalarray = [f"Onesided Pvalue: {OnesidedPvalue:.4f}"]
    elif direction == 'twosided':
        finalarray = [f"Twosided Pvalue: {TwoSidedPvalue:.4f}"]
    elif direction != 'both' and direction != 'onesided' and direction != 'twosided':
        finalarray = perm_differences
    return finalarray

print(f"Onesided Pvalue: {permutation_function(holdout_array, test_array, 10000, 'both')}")

# building a quick frequency chart
plt.hist(permutation_function(holdout_array, test_array, 10000, ''), bins=10)
plt.xlabel("ObsMeanDiff")
plt.ylabel("Frequency")
plt.title("Histogram of ObsMeanDiff")
plt.axvline(np.percentile(permutation_function(holdout_array, test_array, 10000, ''), 10),
           alpha = 0.45,
           color = 'red',
           linestyle = 'dashed',
           label = '10th Percentile'
           )
plt.axvline(np.percentile(permutation_function(holdout_array, test_array, 10000, ''), 90),
           alpha = 0.45,
           color = 'red',
           linestyle = 'dashed',
           label = '90th Percentile'
           )
plt.legend()
plt.show()