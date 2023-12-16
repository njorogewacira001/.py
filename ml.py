import pandas as pd
import numpy as np

# Create a sample DataFrame with null values
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, 4, 5],
        'C': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# 1. Detect null values using isnull()
print("\n1. Detect Null Values:")
print(df.isnull())

# 2. Detect non-null values using notnull()
print("\n2. Detect Non-Null Values:")
print(df.notnull())

# 3. Remove rows with null values using dropna()
df_dropna = df.dropna()
print("\n3. DataFrame after Removing Rows with Null Values:")
print(df_dropna)

# 4. Fill null values with a specific value using fillna()
df_fillna = df.fillna(0)  # Fill with 0, you can replace it with any desired value
print("\n4. DataFrame after Filling Null Values:")
print(df_fillna)

# 5. Replace specific values using replace()
df_replace = df.replace(np.nan, -1)  # Replace NaN with -1, you can replace it with any desired value
print("\n5. DataFrame after Replacing Specific Values:")
print(df_replace)

# 6. Interpolate to fill null values using interpolate()
df_interpolate = df.interpolate()
print("\n6. DataFrame after Replacing Specific Values:")
print(df_interpolate)
