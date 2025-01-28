import pandas as pd
class FeatureEngineering:
    def __init__(self, data):
        self.data = data
        self.df = pd.read_csv(self.data, index_col='TransactionId', parse_dates=['TransactionStartTime'])
        
    def create_aggregate_features(self):
        # total transaction amount per customer
        # Total Transaction Amount per Customer
        self.df['TotalTransactionAmount'] = self.df.groupby('CustomerID')['TransactionAmount'].transform('sum')

        # Average Transaction Amount per Customer
        self.df['AverageTransactionAmount'] = self.df.groupby('CustomerID')['TransactionAmount'].transform('mean')

        # Transaction Count per Customer
        self.df['TransactionCount'] = self.df.groupby('CustomerID')['TransactionAmount'].transform('count')

        # Standard Deviation of Transaction Amounts per Customer
        self.df['TransactionStdDev'] = self.df.groupby('CustomerID')['TransactionAmount'].transform('std')
    
    def extract_features(self):
        # Convert 'TransactionDate' to datetime
        self.df['TransactionDate'] = pd.to_datetime(self.df['TransactionDate'])

        # Extract features
        self.df['TransactionHour'] = self.df['TransactionDate'].dt.hour
        self.df['TransactionDay'] = self.df['TransactionDate'].dt.day
        self.df['TransactionMonth'] = self.df['TransactionDate'].dt.month
        self.df['TransactionYear'] = self.df['TransactionDate'].dt.year
        
    def encode_categorical_variables(self):
        df_encoded = pd.get_dummies(self.df, columns=['CategoryColumn'])
