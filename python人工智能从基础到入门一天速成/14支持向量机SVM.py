import numpy as np
import matplotlib.pyplot as mp
import sklearn.svm as svm
import sklearn.model_selection as ms
import sklearn.metrics as sm
#导入数据
data = np.loadtxt('1.txt', delimiter=',')
x = data[:, :2].astype('f8')
y = data[:, -1].astype('f8')
print(x.shape, y.shape)
# 拆分测试集与训练集
train_x, test_x, train_y, test_y = ms.train_test_split(
        x, y, test_size=0.25, random_state=3)
# 构建SVM模型
model = svm.SVC(kernel='rbf', gamma=0.01, C=600)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n),
                             np.linspace(b, t, n))
mesh_x = np.column_stack(
    (grid_x.ravel(), grid_y.ravel()))     #形成25000*2的矩阵
mesh_z = model.predict(mesh_x)
grid_z = mesh_z.reshape(grid_x.shape)

mp.figure('SVM Classification', facecolor='lightgray')
mp.title('SVM Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1],
           c=test_y, cmap='brg', s=80)
mp.show()
