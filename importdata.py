import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('2018_gddp.xlsx')
print(df.tail())
print(df.info())
print("shape of the dataset is",df.shape)
df["Primary"][1]
