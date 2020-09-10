import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
#数据集
exam_data = {
    '学习天数':[0.50, 3.73, 2.00, 3.00, 0.75, 4.00, 1.65, 2.05, 5.00, 1.78, 3.21, 6.68, 2.78, 4.01, 3.57, 2.29, 2.98, 3.19, 2.50, 1.44],
    '答卷时长(min)':[5,    80,   70,   90,   20,   70,   70,   90,   50,   20,   75,   40,   40,   66,   63,  43,    30,   77,   90,   60],
    '是否通过':[  0,    1,    0,    1,    0,    1,    0,    1,    1,    0,    1,    1,    0,    1,    1,    0,    0,    1,    1,    0]
}
exam_sort = pd.DataFrame(exam_data)
print(exam_sort)
exam_X = exam_sort.loc[:, ['学习天数','答卷时长(min)']]
exam_Y = exam_sort.loc[:, '是否通过']
#建立训练数据和测试数据
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(exam_X, exam_Y, train_size= 0.8, test_size= 0.2)
print('原始数据特征：',exam_X.shape,'训练数据特征：',X_train.shape, '测试数据特征：',X_test.shape)
print('原始数据标签：',exam_Y.shape,'训练数据标签：',Y_train.shape, '测试数据标签：',Y_test.shape)
#导入逻辑回归
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear')
#训练模型
model.fit(X_train, Y_train)
print('评估测试集准确率：',model.score(X_test, Y_test))
#预测某学生学习了2.5天，答题时长90分钟能否通过考试
pred = model.predict([[2.5, 90]])
print('能否通过：', pred)
prob = model.predict_proba([[2.5, 90]])
print('实际概率：', prob) #返回0标签和1标签的概率