import numpy as np
import pandas as pd

from Packages import *
from DataToLoad import *

# For this script, the main data that's going to be normalized is the dollar amounts in the transaction table

class NormalizationFunctions:
    @staticmethod
        # Creating a function that normalizes the dataset using min/max normalization
    def MinMaxNormalization():
        TransactionDataDf['MinMaxDollarsNormalized'] = \
            (TransactionDataDf['TransactionAmount'] - np.min(TransactionDataDf['TransactionAmount'])) / \
            (np.max(TransactionDataDf['TransactionAmount']) - np.min(TransactionDataDf['TransactionAmount']))
        return TransactionDataDf['MinMaxDollarsNormalized']
    @staticmethod
        # Creating a function to standardize all the values by converting them to z-scores
    def ZScoreNormalization():
        TransactionDataDf['ZScoreNormalization'] = \
            (TransactionDataDf['TransactionAmount'] - np.mean(TransactionDataDf['TransactionAmount'])) / \
            np.std(TransactionDataDf['TransactionAmount'])
        return TransactionDataDf['ZScoreNormalization']
    @staticmethod
        # Creating a function that normalizes all the values by converting them to ln(x)
    def NaturalLogarithm():
        TransactionDataDf['LnNormalization'] = np.log(TransactionDataDf['TransactionAmount'])
        return TransactionDataDf['LnNormalization']
    @staticmethod
        # creating a function that standardizes all the values by using the IQR normalization method
    def IQRNormalization():
        TransactionDataDf['IQRNormalization'] = (
                (TransactionDataDf['TransactionAmount'] - np.median(TransactionDataDf['TransactionAmount'])) / \
                    (np.percentile(TransactionDataDf['TransactionAmount'], 0.75) - np.percentile(TransactionDataDf['TransactionAmount'], 0.25)))
        return TransactionDataDf['IQRNormalization']

# Creating the new columns for the TransactionDataDf
NormalizationFunctions.MinMaxNormalization()
NormalizationFunctions.ZScoreNormalization()
NormalizationFunctions.NaturalLogarithm()
NormalizationFunctions.IQRNormalization()

# Checking to make sure all the data accounted for
print(TransactionDataDf)