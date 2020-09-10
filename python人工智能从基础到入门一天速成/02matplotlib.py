import numpy as np
import matplotlib.pyplot as mp
#绘制V字型
mp.subplot(2, 2, 1)
x = np.array([1, 2, 3])
y = np.array([4, 0, 4])
mp.plot(x, y)

#绘制垂直线和水平线
mp.subplot(2, 2, 2)
mp.hlines(1, 1, 1.5)  #水平线
mp.vlines([2.5, 3], [0.5, 0.5], [1.5, 1.5])
mp.plot(x, y)

#标记特定点
mp.subplot(2, 2, 3)
mp.scatter(2, 0, color='g',marker='o', label='smaple points', edgecolors='b', s=200 )
mp.plot(x, y)
mp.legend()    #显示图例
mp.show()
