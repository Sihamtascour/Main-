import pandas as pd

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Perform some basic data analysis
summary = data.describe()

# Print summary statistics
print("Summary Statistics:")
print(summary)

# Find and print the correlation matrix
correlation_matrix = data.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Save the summary statistics to a new CSV file
summary.to_csv('summary_statistics.csv')

# Save the correlation matrix to a new CSV file
correlation_matrix.to_csv('correlation_matrix.csv')
