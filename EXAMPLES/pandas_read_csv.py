import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    '../DATA/sales_records.csv',
    dtype={'Order ID': object},
    parse_dates=['Order Date', 'Ship Date'],
)  # Read CSV data into dataframe. Pandas automatically uses the first row as column names

print(df.describe())  # Get statistics on the numeric columns (use `df.describe(include='O')` for text columns)
print()

print(df.info())  # Get information on all the columns ('object' means text/string)
print()

print(df.head(5))  # Display first 5 rows of the dataframe (`df.describe(__n__)` displays n rows)

# df['new column name'] = some expression
df['total_sales'] = df['Units Sold'] * df['Unit Price']
print(df)

print(df.info())
print(df.describe())

my_date = pd.to_datetime('20130101')

df2 = df[(df['Order Date'] < my_date) & (df['Country'] == 'Afghanistan')]
print(df2)

print(df2.iloc[1])
print(df2['Units Sold'].max())
print(df2['Unit Cost'].mean())
print(df2['Units Sold'].sum())
print('-' * 60)

country_counts = df['Country'].value_counts()
print(f"country_counts: {country_counts}")

country_counts.plot(kind='barh')
plt.show()
