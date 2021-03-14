import pandas as pd

PATH_FILE = "test_data.csv"
df_house = pd.read_csv(PATH_FILE)
print(type(df_house))
print(df_house.shape)
print(df_house.columns)
print(df_house[0 : 4])
print(df_house[0 : 4][["ของใช้","Dinner"]])
print(df_house.describe())
print(df_house)

