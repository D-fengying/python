#傅里叶变换：对一条周期曲线进行拆解的过程，最终得到一组光滑的正弦曲线。
import numpy as np
import matplotlib.pyplot as mp
x = np.linspace(0, np.pi*4, 1000)
#叠加1000条曲线
n = 1000
y = np.zeros(n)
for i in range(1, n + 1):
    y += 4 / (2 * i - 1) * np.pi * np.sin((2 * i - 1) * x)
mp.grid(linestyle=':')
mp.plot(x, y)
#对合成曲线进行傅里叶变换
import numpy.fft as nf
complex_ary = nf.fft(y) #获取复数数组
y2 = nf.ifft(complex_ary)   #逆向傅里叶变换
#绘制频域图像
freqs = nf.fftfreq(y2.size, x[1] - x[0])  #通过采样数理与周期获取fft的频率数组
pows = np.abs(complex_ary)      #获取能量 即复数里点到原点距离
mp.grid(linestyle=':')
mp.plot(freqs[freqs > 0], pows[freqs > 0])
mp.show()

