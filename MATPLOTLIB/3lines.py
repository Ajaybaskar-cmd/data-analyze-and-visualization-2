from matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,2)
y=x
y2=x**2
print(x,y)

plt.plot(x,y,marker='.',mfc='k',mec='k',ms=10,ls='dotted',lw=1,c='r')
plt.title("EXAMLE OF THE LINE")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x,y2)
plt.show(block=True)