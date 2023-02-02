import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


plt.style.use('fivethirtyeight')

pd.set_option('display.max_columns', 89)

# Global Variables
StartDate = '2015-01-01'
EndDate = '2022-01-01'

# Initial DataFrame of Imported Clean Data
df = pd.read_csv('Data/CustomerQuotedProduct_clean.csv', encoding='Latin-1')
df.info()

# Filtered DataFrame of Cleaned Data
df2 = df.loc[(df['fldDate'] >= StartDate) & (df['fldDate'] < EndDate)]
df2.head()

# EDA Value counts to understand top specified Product lines.
df2['fldGroupTypeID'].value_counts()
df2['fldManufacturer_ID'].value_counts()
df2['fldFurnitureSystemID'].value_counts()

# (Line count) of Furniture Catagories Quoted
plt.figure(figsize=(15, 5))
sns.countplot(x='fldGroupTypeID', data=df2)
plt.title(f'{StartDate} - {EndDate} furniture Catagories Count')
plt.xlabel('Furniture Catagories Quoted')

# (Line Count) of Parts by Type that was Quoted.
plt.figure(figsize=(15, 40))
sns.histplot(y='fldOpsWorksheetID', data=df2)
plt.title(f'{StartDate} - {EndDate} Groups Count')
plt.ylabel('Furniture System Catagories')
plt.xlabel('count of entries')

# (Line Count) of Manufacturer Entries.
plt.figure(figsize=(10, 30))
sns.histplot(y='fldManufacturer_ID', data=df2)
plt.title(f'{StartDate} - {EndDate} Manufacturers Quoted')
plt.ylabel('Manufacturers')
plt.xlabel('count of Quoted lines')

# Example of a Query statement.
df.query('fldQuantity == 196')
GroupID = df2.groupby('fldManufacturer_ID')
GroupID['fldQuantity'].sum()
