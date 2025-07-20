import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,1000)
n = np.arange(0,11,1)
scale = float(input('enter scale factor:'))

fig,a = plt.subplots(2,1)
a[0].set_title(" continuos scale ramp")
a[0].plot(t*scale,t)
a[0].grid(True)

a[1].set_title(" discrete scale ramp")
a[1].stem(n,n*scale)
a[1].grid(True)

plt.tight_layout()
plt.show()