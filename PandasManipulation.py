# Manipulating data using Pandas

from DataToLoad import *
from Packages import *

# We already declared both data frames as a pandas data frame in DataToLoad.py

# Joining dataframes using pandas
JoinedTables = CustomerDataDf.merge(TransactionDataDf, on='CustomerId', how='left')

# Doing a few aggregate functions to see a few different statistics
QuickSummary = JoinedTables.groupby('CustomerId').agg(
    MeanTransaction = ('TransactionAmount', 'mean'),
    MedianTransaction = ('TransactionAmount', 'median'),
    RangeofTransaction = ('TransactionAmount', 'std'),
    LowestTransaction = ('TransactionAmount', 'min'),
    HighestTransaction = ('TransactionAmount', 'max'),
    NumberofTransactions = ('TransactionId', 'count')
)

# Filtering to get only transactions that are 50$ or more
TransactionsOver50 = JoinedTables.groupby('TransactionId')\
    .filter(lambda x: x['TransactionAmount'] >= 50.00)

# Only give me customers that spent a total of 120 or more
CustomersSpentOver120 = JoinedTables.groupby('CustomerId')\
    .filter(lambda x: x['TransactionAmount'].sum() >= 120.00)

# Looking at customers in Canada
CustomersInCanada = JoinedTables[(JoinedTables['Country'] == 'Canada')]

# Looking at customers in US who spent a total of over $40
CustomersInUSOver40Dollars = JoinedTables.groupby('CustomerId')\
    .filter(lambda x: (x['TransactionAmount'].sum() >= 40))\
    .loc[(JoinedTables['Country'] == 'USA')]

# Looking at breakdown of Gender by Country
GenderByCountry = JoinedTables.groupby(['Country', 'Gender']).agg(
    NumberofTransactions = ('TransactionId', 'count'),
    NumberofCustomers = ('CustomerId', 'nunique'),
    TotalPaidTransaction = ('TransactionAmount', 'sum'),
)