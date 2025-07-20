import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,60)
value = len(x) // 4

sine =np.sin(x)
cosine = np.cos(x)
ramp = x
impulse = np.zeros(len(x))
impulse[2*value] = 1
rect = np.where(np.abs(x)<=5,1,0)
bipolar = np.concatenate((np.zeros(value),np.ones(value),-np.ones(value),np.zeros(value)))
triangular = np.concatenate((-10-x[0:value],x[value:3*value],10-x[3*value:]))

fig,a=plt.subplots(2,4)
a[0,0].plot(x,sine)
a[0,1].plot(x,cosine)
a[0,2].plot(x,ramp)
a[0,3].plot(x,impulse)
a[1,0].plot(x,rect)
a[1,1].plot(x,bipolar)
a[1,2].plot(x,triangular)

fig,b=plt.subplots(2,4)
b[0,0].stem(x,sine)
b[0,1].stem(x,cosine)
b[0,2].stem(x,ramp)
b[0,3].stem(x,impulse)
b[1,0].stem(x,rect)
b[1,1].stem(x,bipolar)
b[1,2].stem(x,triangular)
plt.show()
