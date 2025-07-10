import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Series

list1 = pd.Series([1,1,3], index = ["first","second","third"])
# print(list1)
# print(list1 + 10)



list2 = list1.apply(lambda x: x*100)
list2.index = [1,2,3]

# print(list2)

# print(list1.nunique())
# print(list1.unique())

# print(list1.value_counts())
# help(list1)

list2 = pd.Series([10,20,30], index = ["first","second","third"])
mult = list1 * list2
# print(mult)
# print('The sum: ', mult.sum())




#DataFrame
# names = ['Aa','Bb','Cc']
# ages = [18,12,45]
# cities = ['Abovyan', 'Erevan', 'Dilijan']
# df = pd.DataFrame({'Name': names, 'Age': ages, 'City': cities})

# print(df)


# CSV -> Comma Seperated Values

df = pd.read_csv("teen_phone_addiction_dataset.csv")

df = df[['Name', 'Age', 'Daily_Usage_Hours','Addiction_Level']]
df = df.rename(columns={
    'Daily_Usage_Hours': 'Hrs/Day',
    'Addiction_Level': 'Add_Lvl'
})
# print(df.head())
# print(df.tail())

# print(df['Hrs/Day'].value_counts().sort_index())

# df = df.set_index('Name')
# print(df.iloc[0:10])

# print(df.iloc[0,0])

# print(df.iloc[0:10, 0:2])

# print(df.loc[5,'Age'])

_df = df.iloc[0:10, :]
# print(_df)
# _df = _df.drop([1,2,3], axis = 0)  #or -> _df = _df.drop(index= [1,2,3]) 
# print(_df)

# df_names = _df.loc[:,'Name']
# print(_df['Age'])
# print(df_names)

# _df['DOB'] = 2025 - _df['Age'] 
# print(_df)


# print(df[df['Hrs/Day'] > 10])

# print(len(df[df['Hrs/Day'] > 10]))

# gruped = df.groupby('Age')

# for name, group in gruped:
#     print(name)
#     print(group.head())
#     print('/n')

pivot_table = df[df["Age"] < 16].pivot_table(index = 'Hrs/Day', columns= 'Age', values= 'Add_Lvl', aggfunc= ['count', 'sum'], margins=True)
pivot_table = pivot_table.fillna('-') #or-> pivot_table.fillna('-',inplace=True)
pivot_table.replace({1.0 : 1,
                     2.0 : 2,
                     3.0 : 3,
                     4.0 : 4,
                     5.0 : 5}, inplace=True)
print(pivot_table)


# To save 
# df.to_csv("new_data", index=False)  # Dandax e
df.to_parquet("new_data2", index=False)