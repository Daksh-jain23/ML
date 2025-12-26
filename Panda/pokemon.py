import pandas as pd

df = pd.read_csv("D:\\Code\\Python\\Class\\My Class\\DataSet\\kagglehub\\Pokemon\\pokemonGen1.csv", index_col = "Name")

print(df.loc["Charizard":"Moltres", ["Type1","Legendary"]])
print( df[["Type1", "Type2"]])
print(df.iloc[-3:, 0:3].to_string())
print()

# name = input("Enter Name:")
# try:
#     print(df.loc[name])
# except KeyError:
#     print(f"{name} not found")

#filtering

# print(df[df["Height"] > 1])

print(df[df["Weight"] > 100])