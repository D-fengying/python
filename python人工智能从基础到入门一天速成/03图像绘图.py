import numpy as np
import matplotlib.pyplot as mp
#绘制窗口
mp.figure(facecolor='lightgray')
mp.title('fill', fontsize=18)
x = np.linspace(0, 10, 1000)
sinx = np.sin(x)
cosx = np.cos(x / 2) / 2
mp.grid(linestyle=':', color='r')
mp.plot(x, sinx, label=r'$y=sin(x)$')
mp.plot(x, cosx, color='orangered',
        label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')
mp.legend()
#填充颜色
mp.fill_between(x, sinx, cosx, sinx > cosx,
                color='dodgerblue', alpha=0.3)
mp.fill_between(x, sinx, cosx, sinx < cosx,
                color='orangered', alpha=0.3)
mp.legend()
mp.show()
#绘制柱形图
xiaoming = np.array([57, 55, 58, 49, 52, 43, 59])
xiaohong = np.array([95, 90, 97, 83, 87, 80, 99])
mp.figure('Bar', facecolor='lightgray')
mp.title('Bar Chart', fontsize=18)
mp.grid(linestyle=':')
x = np.arange(xiaoming.size)
mp.bar(x - 0.2, xiaoming, 0.4, color='limegreen',
       label='xiaoming', align='center')
mp.bar(x + 0.2, xiaohong, 0.4, color='orangered',
       label='xiaohong', align='center')
mp.xticks(x, ['yuwen','shuxue','yingyu','wuli','huaxue','zhengzhi','lishi'])
mp.legend()
mp.show()
#绘制饼状图
values = [57, 55, 58, 49, 52, 43, 59]
spaces = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.05]
labels = ['yuwen','shuxue','yingyu','wuli',
          'huaxue','zhengzhi','lishi']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold','blue', 'red']
mp.figure('Pie Chart')
mp.pie(values, spaces, labels, colors,
       '%.1f%%', shadow=True)
mp.legend()
mp.show()