import numpy as np
import pandas as pd

consumer = ['Amit', 'Rahul', 'Priya', 'Sneha', 'Rohan']
bills = np.array([2500, 3500, 1800, 4200, 3000])

print("Mean:", np.mean(bills))
print("Median:", np.median(bills))
print("Maximum:", np.max(bills))
print("Minimum:", np.min(bills))

df = pd.DataFrame({
    'Consumer': consumer,
    'Bill': bills
})

print("\nAll Consumer Records:")
print(df)

print("\nConsumers with bills above 3000:")
print(df[df['Bill'] > 3000])
