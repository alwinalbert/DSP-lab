import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,1000)
n = np.arange(0,11,1)

fig , a = plt.subplots(2,1)

a[0].set_title("reversed continuos ramp")
a[0].plot(-t,t)
a[0].grid(True)

a[1].set_title("reversed discrete ramp")
a[1].stem(-n,n)
a[1].grid(True)

plt.tight_layout()
plt.show()


