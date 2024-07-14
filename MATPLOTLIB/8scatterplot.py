from matplotlib import pyplot as plt
import random
import numpy as np
x=np.arange(1,11)
y=x*10
random.shuffle(y)
print(x,y)

plt.scatter(x,y,color='red',marker='*')
#plt.show(block=True)

x1=np.arange(1,11)
y1=x*10

random.shuffle(x1)
print(x1,y1)

plt.scatter(x1,y1,color='green',marker='^',linewidth=10)
plt.show(block=True)
