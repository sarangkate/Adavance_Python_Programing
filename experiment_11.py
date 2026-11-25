import pandas as pd
import random


ser = pd.Series([random.randint(1, 100) for i in range(10)])

print("Pandas Series:")
print(ser)

df = pd.DataFrame({
    'Name': ['Amit', 'Rahul', 'Priya'],
    'Marks': [80, 90, 85]
})

print("\nDataFrame:")
print(df)

print("\nMarks:")
print(df['Marks'])

print("\nFirst Row:")
print(df.iloc[0])
