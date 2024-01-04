import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('9780596153946/historical_sales_data.xls')
df = df.dropna(subset=['Month', 'Year', 'Fish', 'Ducks', 'Total '])

fish_array = df['Fish'].values
duck_array = df['Ducks'].values
total_array = df['Total '].values
month_array = df['Month'].values

plt.plot(df.index, fish_array, label='Fish')
plt.plot(df.index, duck_array, label='Duck')
plt.plot(df.index, total_array, label='Total')

plt.xticks(df.index, month_array)
plt.ylabel('Units Sold')
plt.title('Sales History')
plt.legend()
plt.savefig('report/figures/historical_sales.png')
plt.show()

