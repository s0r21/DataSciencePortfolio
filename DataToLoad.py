# Data set to run analysis on around with
import pandas as pd

from Packages import *

def CustomerDataFunction():
    CustomerData = {
    'CustomerId' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'CustomerName' : ['Nathan', 'John', 'Brandon', 'Stacy', 'Jordan', 'Tyler', 'Jarred', 'Adam', 'Samantha', 'Megan'],
    'PhoneNumber' : ['265-4930', '888-9090', '780-5614', '314-6507', '945-1234', '679-9069', '305-2342', '134-5690',
                     '670-4990', '560-2031'],
    'Gender' : ['M', 'M', 'M', 'F', 'M', 'M', 'M', 'M', 'F', 'F'],
    'Country' : ['Canada', 'USA', 'USA', 'USA', 'Canada', 'USA', 'Canada', 'Canada', 'Canada', 'USA']
    }
    return pd.DataFrame(CustomerData)

def TransactionDataFunction():
    TransactionData = {
        'TransactionId' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        'CustomerId' : [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 8, 4, 2],
        'TransactionAmount' : [29.59, 31.27, 22.01, 30.80, 50.60, 42.91, 19.99, 15.99, 23.91, 22.69,
                               31.45, 19.42, 67.99, 31.63, 51.29, 33.33, 19.51, 96.71, 41.49, 22.22],
        'Currency': ['CAD', 'CAD', 'CAD', 'CAD', 'CAD', 'USD', 'USD', 'USD', 'CAD', 'USD',
                     'CAD', 'CAD', 'CAD', 'USD', 'CAD', 'USD', 'USD', 'CAD', 'USD', 'USD']
    }
    return pd.DataFrame(TransactionData)

# Creating a Pandas data frame. Using Pandas over Spark due to size of the dataset.
CustomerDataDf = CustomerDataFunction()
TransactionDataDf = TransactionDataFunction()

# Making sure the data is in the dataframe
# print(CustomerDataDf.head())
# print(TransactionDataDf.head())