from matplotlib import pyplot as plt
import numpy as np

x=np.arange(0,10,2)
y=x**2
#print(x)
#print(y)

plt.plot(x,y,marker='*',mec='r',mfc='g',ms=10)
plt.title('MARKER')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show(block=True)
