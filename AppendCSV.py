import pandas as pd

# List of CSV file paths
csv_files = ["reviews.csv", "reviews-1.csv", "reviews-2.csv", "reviews-3.csv", "reviews-4.csv"]

# Create an empty DataFrame to hold the combined data
dfs = []

# Loop through each CSV file and append its data to the list
for file in csv_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate the list of DataFrames into a single DataFrame
combined_data = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_data.to_csv("combined.csv", index=False)

print("CSV files appended and combined successfully.")
