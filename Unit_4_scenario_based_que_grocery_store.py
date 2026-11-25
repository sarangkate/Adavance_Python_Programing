import numpy as np
import pandas as pd

items = ['Rice', 'Sugar', 'Wheat', 'Oil', 'Salt']
prices = np.array([600, 450, 550, 900, 200])
quantity = [15, 8, 20, 5, 12]

print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

df = pd.DataFrame({
    'Item': items,
    'Price': prices,
    'Quantity': quantity
})

print("\nAll Grocery Records:")
print(df)

print("\nItems with Quantity less than 10:")
print(df[df['Quantity'] < 10])
