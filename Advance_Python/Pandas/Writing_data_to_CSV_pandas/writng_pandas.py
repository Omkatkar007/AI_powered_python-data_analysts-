import pandas as pd 

# wrting data to csv

df = pd.DataFrame({'Name':['John', 'Mary', 'Tom', 'John'],
                   'Age':[20, 25, 30, 20],
                   'City':['New York', 'London', 'Paris', 'New York']})

df.to_csv('data.csv', index=False)

# multiple sheets

df1 = pd.DataFrame({'Name':['John', 'Mary', 'Tom', 'John'],
                   'Age':[20, 25, 30, 20],
                   'City':['New York', 'London', 'Paris', 'New York']})

df2 = pd.DataFrame({'Name':['John', 'Mary', 'Tom', 'John'],
                   'Age':[20, 25, 30, 20],
                   'City':['New York', 'London', 'Paris', 'New York']})

with pd.ExcelWriter('data.xlsx') as writer: 
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')


# apending data to csv

df = pd.DataFrame({'Name':['John', 'Mary', 'Tom', 'John'],
                   'Age':[20, 25, 30, 20],
                   'City':['New York', 'London', 'Paris', 'New York']})                   

df.to_csv('data.csv', index=False, mode='a')  


# controlling output format

df = pd.DataFrame({'Name':['John', 'Mary', 'Tom', 'John'],
                   'Age':[20, 25, 30, 20],
                   'City':['New York', 'London', 'Paris', 'New York']})                   

# change separator
df.to_csv('data.csv', sep=';', index=False, mode='a')

# control missing values

df = pd.DataFrame({'Name':['John', 'Mary', 'Tom', 'John'],
                   'Age':[20, 25, 30, 20],
                   'City':['New York', 'London', 'Paris', 'New York']})                   
                   
df.to_csv('data.csv', na_rep='NA', index=False, mode='a')   

# saving only specific columns

df = pd.DataFrame({'Name':['John', 'Mary', 'Tom', 'John'],
                   'Age':[20, 25, 30, 20],
                   'City':['New York', 'London', 'Paris', 'New York']})             

df.to_csv('data.csv', columns=['Name', 'Age'], index=False, mode='a')       