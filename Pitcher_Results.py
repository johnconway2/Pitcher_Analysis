import pandas as pd

df = pd.read_csv("Pitcher_data.csv")
list_of_column_names=list(df.columns)
print("List of column names:", list_of_column_names)