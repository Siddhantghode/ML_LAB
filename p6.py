import pandas as pd
df=pd.read_csv("Car data.csv")
print(df.head())
print("\n")
print(df.tail())
print("\n")
print(df.describe())
print("\n")

print(df.info())
print("\n" )

print(df.shape())
print("\n")
