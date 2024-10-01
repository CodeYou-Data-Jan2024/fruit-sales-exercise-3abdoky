import pandas as pd

# Create a dictionary for the data
data = {
    "Apples": [35, 41],
    "Bananas": [21, 34]
}

# Create a list of row labels
index = ["2017 Sales", "2018 Sales"]

# Create the DataFrame
df = pd.DataFrame(data, index=index)

# Write the DataFrame to a CSV file
df.to_csv("fruit.csv")

print("DataFrame written to fruit.csv")