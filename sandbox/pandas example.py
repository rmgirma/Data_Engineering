import pandas as pd

file_path = 'C:\Misc\AppleStore.csv'
opened_file = open(file_path, encoding="utf8")
df = pd.read_csv(file_path)
opened_file.close()

df.info()
# a = df.head()
# print(a)
# b = df.tail()
# print(b)
# print(df.shape[0]) # prints the number of rows
# print(df.shape[1]) # prints the number of columns

print('000000000000000000000000000000000000')
df = df[(df['price'] !=0)]
grouped = df.groupby('prime_genre').agg({'price': ['mean', 'min', 'max','count','sum']})   # ['mean', 'min', 'max'] 
print(df.shape[0]) # prints the number of rows
print(df.shape[1]) # prints the number of columns

print(grouped)

print('11111111111111111111111111111111111111')

two_columns = df[['prime_genre','price']]  # select the referred 2 columns
print(two_columns)
two_columns.to_csv('C:\\Misc\\two_column.csv', index=False)
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

group_by_ex = two_columns.groupby('price').count()              # group by
print(group_by_ex)
print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

expensive = df[(df['price'] >= 0) & (df['cont_rating'] =='4+') & (df['prime_genre'] == 'Games')]  # filter by multiple columns
exp = expensive[['track_name', 'price', 'prime_genre','user_rating']]
exp = exp.sort_values(by=['price','user_rating'],ascending=False)  # sort by 2 columns in descending manner
exp.to_csv('C:\\Misc\\expensive.csv', index=False)
print(exp)
print('ccccccccccccccccccccccccccccccccccccccc')

group_by_expensive = expensive.groupby('prime_genre').count()   # group by columns - count() sum() 
gr = expensive.groupby('price').count()
print(gr)

print('ddddddddddddddddddddddddddddddddddddddd')
import matplotlib.pyplot as plt


two_columns['prime_genre'].value_counts().plot.bar()
# df['prime_genre'].value_counts().plot.pie()
plt.title('Pie Chart of Ratings')               # plot charts pie bar line etc...
# plt.show()

