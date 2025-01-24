# Overview of the Data
import pandas as pd
import matplotlib.pyplot as plt
class EDA:
    def __init__(self, data):
        self.data = data
        self.df = pd.read_csv(self.data, index_col='TransactionId', parse_dates=['TransactionStartTime'])
    
    def sample_of_dataset(self):
        return self.df.sample()
        
    def get_overview_of_the_dataset(self):
        # check the shape of the dataset number of rows and columns
        shape = self.df.shape
        return {"row and columns of dataset":shape, "data type of the dataset":self.df.dtypes}
    def get_summery_statics(self):
        return {"describe":self.df.describe(),"Skewness":self.df.skew(numeric_only=True), "kurtosis": self.df.kurtosis(numeric_only=True)}
    
    def plot_distribution_of_each_column(self):
        self.df.hist(figsize=(20, 20))
        plt.show()