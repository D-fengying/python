#数据预处理
import numpy as np
import sklearn.preprocessing as sp
samples = np.array([
    [20., 2., 4000.],
    [22., 2.5, 4500.],
    [30., 4., 5500.]
])
result = sp.scale(samples)
print(result)   #将数据标准化 即每个样本(X-mean)/std
#范围缩放
mms = sp.MinMaxScaler(feature_range=(0, 1))
result2 = mms.fit_transform(samples)
print(result2)
#归一化
result3 = sp.normalize(samples, norm='l1')
print(result3)
#二值化
erzhihua = sp.Binarizer(threshold=100)
result4 = erzhihua.transform(samples)
print(result4)
