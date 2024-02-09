# see: https://stackoverflow.com/a/59308195
import pandas as pd
# first, read in the csv files
df1 = pd.read_csv('in/sml.csv')
df2 = pd.read_csv('in/big.csv')

# This assumes the data are in a column called `email` (update in both spots if different)
df1['exists'] = df1.email.isin(df2.email)

# and, finally, write out dataframe 3
df1.to_csv('out/compare.csv', index=False)