import pandas as pd

# Read the first CSV file into df1
data1 = pd.read_csv("combined.csv")

# Read the second CSV file into df2
data2 = pd.read_csv("MSA_iOS_Reviews_New.csv")

# Find the differences in the 'title' columns
differences = data1[~data1['title'].isin(data2['title'])]

# Print the differences
differences['title'].to_csv('testData.csv')
