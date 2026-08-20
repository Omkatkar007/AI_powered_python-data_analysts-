# reading csv & excel files using pandas

import pandas as pd 


# reading csv file

df = pd.read_csv('data.csv')
print(df)

#inspect
df.head()  # first 5 rows
df.info()

print(df.head(),df.info())


# common issues in reading csv files:

'''custom delimiter/ separator'''

df = pd.read_csv('data.csv',sep=':')

''' skipping rows '''

df = pd.read_csv('data.csv',skiprows=2)

''' reading only specific columns '''

df = pd.read_csv('data.csv',usecols=[0,1,2])


# reading excel file

df = pd.read_excel('data.xlsx')
print(df)

# excel file with multiple sheets 
df = pd.read_excel('data.xlsx',sheet_name=['Sales_Data','Employee_Metrics'])
print(df)


#  list all sheets in excel file
import pandas as pd

# 1. Read the file as an ExcelFile object (not a DataFrame)
workbook = pd.ExcelFile('data.xlsx').sheet_names
print(workbook)

# handling missing values or broken data while reading 

pd.read_csv('data.csv',na_values=['NA','Missing','?','-'])   #By default, Pandas only recognizes standard empty cells as missing data. If it sees a ? inside a column of prices, it assumes the entire column is made of text.


# setting columns data types while reading 

pd.read_csv('data.csv',dtype={'column1': str, 'column2': float})  #This will ensure that column1 is read as a string and column2 as a float, regardless of the data in the CSV file.

# reading large files in chunks

pd.read_csv('data.csv',chunksize=10000)  #This will read the file in chunks of 10000 rows at a time.