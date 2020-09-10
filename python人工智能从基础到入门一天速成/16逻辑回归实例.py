#已知一部分学生的学习时间和通过考试的情况，预测另一部分学生的通过考试的情况。
# 其中，特征为学习时间，标签为通过考试
import pandas as pd
import matplotlib.pyplot as mp
#数据集
exam_data = {
    '学习时间(天)':[0.50, 3.73, 2.00, 3.00, 0.75, 4.00, 1.65, 2.05, 5.00, 1.78, 3.21, 6.68, 2.78, 4.01, 3.57, 2.29, 2.98, 3.19, 2.50, 1.44],
    '考试是否通过':[  0,    1,    0,    1,    0,    1,    0,    1,    1,    0,    1,    1,    0,    1,    1,    0,    0,    1,    1,    0]
}
exam_sort = pd.DataFrame(exam_data)
print(exam_sort)
#提取特征和标签
exam_X = exam_sort.loc[:, '学习时间(天)']
exam_Y = exam_sort.loc[:, '考试是否通过']
#绘制散点图
mp.scatter(exam_X, exam_Y, color='b', label = "exam_data")
mp.xlabel("day")
mp.ylabel("pass")
mp.show()
#建立训练数据和测试数据
from sklearn.model_selection import train_test_split
#建立训练数据集和测试数据集
X_train, X_test, Y_train, Y_test = train_test_split(exam_X, exam_Y, train_size= 0.8, test_size= 0.2)
print('原始数据特征：',exam_X.shape[0],'训练数据特征：',X_train.shape[0], '测试数据特征：',X_test.shape[0])
print('原始数据标签：',exam_Y.shape[0],'训练数据标签：',Y_train.shape[0], '测试数据标签：',Y_test.shape[0])
mp.scatter(X_train, Y_train,color = 'blue', label = 'train_data')
mp.scatter(X_test, Y_test,color = 'red', label = 'test_data')
mp.show()
#将数据变为1列
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)
#导入逻辑回归
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear')
#训练模型
model.fit(X_train, Y_train)
print('评估测试集准确率：',model.score(X_test, Y_test))
#预测某学生学习了2.5天能否通过考试
pred = model.predict([[2.5]])
print('能否通过：', pred)
prob = model.predict_proba([[2.5]])
print('实际概率：', prob) #返回0标签和1标签的概率