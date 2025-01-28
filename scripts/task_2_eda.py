# Overview of the Data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class EDA:
    def __init__(self, data):
        self.data = data
        self.df = pd.read_csv(self.data, index_col='TransactionId', parse_dates=['TransactionStartTime'])
    
    def sample_of_dataset(self):
        return self.df.sample()
        
    # overview of the dataset
    def get_overview_of_the_dataset(self):
        # check the shape of the dataset number of rows and columns
        shape = self.df.shape
        return {"row and columns of dataset":shape, "data type of the dataset":self.df.dtypes}
    def get_summery_statics(self):
        return {"describe":self.df.describe(),"Skewness":self.df.skew(numeric_only=True), "kurtosis": self.df.kurtosis(numeric_only=True)}
    
    def plot_distribution_of_each_column(self):
        # Histogram for each numerical feature 
        self.df.hist(figsize=(12, 10), bins=20, color='skyblue', edgecolor= 'black')
        plt.suptitle("Histogram for Numerical Features")
        plt.show()
        
        
        # KDE plots for numerical features
        plt.figure(figsize=(12,6))
        for column in self.df.select_dtypes(include=['int64','float64']).columns:
            sns.kdeplot(self.df[column], fill = True, label =column)
        plt.title('KDE Plot of numerical Features')
        plt.legend()
        plt.show()
        
    def distribution_of_categorical_features(self):
        categorical_columns=self.df.select_dtypes(include=['object']).columns
        plt.figure(figsize=(12,8))
        for i, column in enumerate(categorical_columns, 1):
            plt.subplot(len(categorical_columns),1,i)
            sns.countplot(data=self.df, x=column, palette='pastel')
            plt.title(f"Distribution of {column}")
            plt.xticks(rotation=45)
            
        plt.tight_layout()
        plt.show()
        
    def correlation_analysis(self):
        # calculate correlation matrix
        corr_matrix = self.df.corr(numeric_only=True)
        
        # plot heatmap
        plt.figure(figsize=(12, 10))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix')
        plt.show()
    
    def identifying_missing_values(self):
        
        missing_values = self.df.isnull().sum()
        missing_percent = (missing_values / self.df.shape[0]) * 100
        # Visualize missing values
        plt.figure(figsize=(12, 6))
        sns.heatmap(self.df.isnull(), cbar=False, cmap="viridis", yticklabels=False)
        plt.title("Missing Values Heatmap")
        plt.show()
        return pd.concat([missing_values, missing_percent], axis=1, keys=['Missing Values', 'Percentage'])