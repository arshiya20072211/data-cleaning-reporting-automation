import pandas as pd

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Alice', None],
    'Age': [25, 30, 25, 28],
    'Salary': [50000, 60000, 50000, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df['Name'] = df['Name'].fillna('Unknown')
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print("\nCleaned Data:")
print(df)

# Generate summary report
print("\nSummary Report:")
print(df.describe())
