import pandas as pd


dict_data = { "name": ["Alice", "Bob", "Charlie", "David"],
            "marks": [100, 80, 90, 85]}

df = pd.DataFrame(dict_data)
print(df)

df.head()
df.tail()
df.info()
df.describe()

# selecting data 

df["name"]
df["marks"]
df[["name","marks"]]
