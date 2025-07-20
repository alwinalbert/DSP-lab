import numpy as np 
import matplotlib.pyplot as plt

a = eval(input("enter the scale factor:"))
t = np.linspace(-10,10,1000)

rect =lambda x: np.where(np.abs(x)<1,1,0)
plt.title("rectangular scalar function")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.plot(t,rect(t/a))
plt.grid(True)
plt.show()