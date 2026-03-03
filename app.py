import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# df = pd.read_csv("mymoviedb.csv" )
df = pd.read_csv(
    "mymoviedb.csv",
    engine="python",
    encoding="latin1",
    on_bad_lines="skip"
)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nBasic Statistics:")
print(df.describe())
print(df.head())

df.info


