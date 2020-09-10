import pandas as pd
import numpy as np

#创建Series对象
ary = np.array([70, 80, 90, 100])
s = pd.Series(ary)
print(s)   #创建Series对象时，指定index行级索引标签
#创建二维列表标签
data = [[80, 81], [70, 71], [90, 91], [60, 61]]
df = pd.DataFrame(data)
print(df)
#字典方法新建列
data2 = {
    'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df2 = pd.DataFrame(data2)
print(df2)
#行访问
print(df2[1:3])
#删除某列
del(df2['two'])
print(df2)
#求平均值
print('----\n',df2.mean())
#排序
sort_one = df2.sort_values(by='one',ascending=False)
print('----\n',sort_one)

#pandas的日期处理
dates = pd.Series(
    ['2011', '2011-02', '2011-03-01', '2011/04/01', '2011/05/01 01:01:01','01 Jun 2011']
)
dates = pd.to_datetime(dates)
print(dates)
