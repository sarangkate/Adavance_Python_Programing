
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Age': [24, 27, 22, 32, 29, 25, 100],
    'Salary': [50000, 60000, 52000, 58000, 62000, 55000, 600000]
}

df = pd.DataFrame(data)

print("Descriptive Statistics:")
print(df.describe())

print("Mean:", df['Age'].mean())
print("Median:", df['Age'].median())

plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


df.loc[2, 'Age'] = None

print("Missing Values:")
print(df.isnull())

df = df.fillna(df.mean())

print("After Filling Missing Values:")
print(df)


Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)

IQR = Q3 - Q1

df_cleaned = df[
    (df['Age'] >= Q1 - 1.5 * IQR) &
    (df['Age'] <= Q3 + 1.5 * IQR)
]

print("After Removing Outliers:")
print(df_cleaned)
