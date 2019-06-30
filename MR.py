# -*- coding: utf-8 -*-
"""
To implement Multirate DSP Techniques
Upsampling
DownSampling
"""

from numpy import linspace,sin,pi
from scipy.signal import upfirdn
import matplotlib.pylab as plt
t=linspace(0,1)
h=sin(2*pi*1*t)

#h=[1,2,3,4]
c=upfirdn(h,[1],up=2,down=2)
y=upfirdn(h,[1])
plt.stem(h)
plt.title('Input signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

plt.stem(y)
plt.title('part 2')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

z=upfirdn(h,[1],up=3)

plt.stem(z)
plt.title('part 3')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.stem(c)
plt.title('Final output')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()


