import pandas as pd 



df = pd.DataFrame({
    "Product Name": [" iPhone 14", "Samsung Galaxy", " OnePlus 11", "Pixel 7 ", None] * 200,
    "price": ["499", "799", "1,199", "899", None] * 200,
    "category": ["Mobile", "mobile", "ELECTRONICS", "Electronics", None] * 200,
    "rating": [5, 4, None, 3, 2] * 200,
    "reviews": [1200, 3400, 560, 780, 150] * 200,
    "in_stock": ["Yes", "No", "yes", "no", None] * 200,
    "launch_year": ["2023", "2022", "2021", "2020", None] * 200
})
# 1. Remove the commas using Pandas vectorization (.str.replace)
df["price"] = df["price"].str.replace(',', '')

# 2. Convert the cleaned text column into numeric data (floats/ints)
# pd.to_numeric automatically handles the 'None' values by turning them into 'NaN' (Not a Number)
df["price"] = pd.to_numeric(df["price"])

#selecting data


print(df['Product Name'])
print(df[['Product Name', 'price']])

# filtering data

print(df[df['price'] > 500])   # condition

print(df[(df['price'] > 500) & (df['category'] == 'Electronics')])    # multiple conditions

# handling missing data

print(df.isna())
df.isna().sum()

df.dropna() # missing values are dropped from the DataFrame

df["rating"] = df["rating"].fillna(df["rating"].mean())  # missing values are filled with the mean of the column

# renaming columns
df = df.rename(columns={"Product Name": "product_name", "price": "price_in_usd", "category": "product_category", "rating": "customer_rating", "reviews": "number_of_reviews", "in_stock": "availability_status", "launch_year": "year_of_launch"})

# changing data types

print(df.dtypes) # returns the data types of the columns

df["price"] = df["price"].astype(float) # changing the data type of the column to float

# removing duplicates
df.drop_duplicates() # removes duplicate rows from the DataFrame

# basic string cleaning

df["category"] = df["category"].str.lower().str.strip() # converts the text to lowercase and removes leading/trailing whitespace
