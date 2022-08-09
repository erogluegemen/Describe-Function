import statistics
import pandas as pd
import numpy as np
from collections import Counter


class helper:
    def __init__(self, df):
        self.df = df

    def numeric_describe(self):
        print(f"""
    - Count: {len(self.df)}        
    - Mean: {statistics.mean(self.df)}
        * F Mean: {statistics.fmean(self.df)}
        * Harmonic Mean: {statistics.harmonic_mean(self.df)}
        * Geometric Mean: {statistics.geometric_mean(self.df)}
    - Median: {statistics.median(self.df)}
        * Median Low: {statistics.median_low(self.df)}
        * Median High: {statistics.median_high(self.df)}
    - Mode: {statistics.mode(self.df)}
    - Standart Deviation: {statistics.stdev(self.df)}
    - Variance: {statistics.variance(self.df)}
    - Min: {self.df.quantile(.0)} 
    - %25: {self.df.quantile(.25)}
    - %50: {self.df.quantile(.5)}
    - %75: {self.df.quantile(.75)}
    - Max: {self.df.quantile(1)}
                """)


    def categorical_describe(self):
        print(f"""
    - Count: {len(self.df)}
    - Unique: {len(np.unique(self.df))}
    - Top: {max(set(self.df), key=self.df.count)}
    - Freq: {max(list(Counter.values(self.df.to_dict())))}
               """)
        
        
    def check_df(self, df, head=5):  # df.sample(n=5, random_state=0)
    print("##################### Shape #####################")
    print(self.df.shape)

    print("##################### Types #####################")
    print(self.df.dtypes)

    print("##################### Head #####################")
    print(self.df.head(head))

    print("##################### Tail #####################")
    print(self.df.tail(head))

    print("##################### NA #####################")
    print(self.df.isnull().sum())

    print("##################### Quantiles #####################")
    print(self.df.quantile([0, 0.25, 0.50, 0.75, 0.99, 1]).T)
    print(self.df.describe().T)


h = helper()  # write your dataframe or column here.
h.numeric_describe()
h.categorical_describe()
h.check_df()
