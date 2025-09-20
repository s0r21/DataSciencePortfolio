# script created for bootstrapping method
import random

from sklearn.utils import resample

from Packages import *


RandomArray = pd.DataFrame(list(random.sample(range(1500), 1000)))

# creating an array to append the medians in
ResultsArray = []

# for loop to take the median of the resamples and then appending the median to the array above
for i in range(0,10000):
    sample = resample(RandomArray)
    ResultsArray.append(sample.median()[0])

# turning the array into a dataframe
Results = pd.DataFrame(ResultsArray)

# Some quick statistics
print('Bootstrap Results:')
# taking the median of the original array
print(f'original median: {RandomArray.median()}')
# quick check bias (how far is our sample mean from our bootstrapped median)
print(f'bias: {Results.mean() - RandomArray.median()}')
# std error to check how the means of the boostrap vary
print(f'std. error: {Results.std()}')

# plotting the results of the original
OriginalHisto = RandomArray.hist(column=[0], bins=10)
OriginalHisto[0][0].set_title('Original Histogram')
OriginalHisto[0][0].set_xlabel('Bins')
OriginalHisto[0][0].set_ylabel('Frequency')

# plotting the results of the bootstrap
ResultsHisto = Results.hist(column=[0], bins=10)
ResultsHisto[0][0].set_title('Bootstrap Histogram')
ResultsHisto[0][0].set_xlabel('Bins')
ResultsHisto[0][0].set_ylabel('Frequency')