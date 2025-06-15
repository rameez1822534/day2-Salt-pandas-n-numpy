import pandas as pd 

df = pd.read_csv('assessment.csv')


df = df[df['Price'].notna()]


df['Category'] = df['Category'].replace(r'[^A-Za-z0-9_]', '', regex=True)


df = df.groupby(['Category', 'Material'])['Price'].mean().reset_index().round(2).reset_index(name='AveragePrice')


#df = df.rename(columns={'Price': 'AveragePrice'})


print(df)
