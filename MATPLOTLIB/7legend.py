from matplotlib import pyplot as plt
import numpy as np
#x=[1,2,3,4,5]
#y=[i**2 for i in x]
#plt.plot(x,y,label='SQUARES')
#plt.legend(facecolor='red',framealpha=0.5)
#plt.show(block=True)

x=np.arange(0,5)
y=x**2
y2=x**3

#plt.plot(x,y,x,y2,marker='.',mfc='k',mec='k')
#plt.legend(['squres','cubes'],edgecolor='black')
plt.plot(x,y,label='SQUARES')
plt.plot(x,y2,label='CUBES')
plt.legend(loc='upper left',framealpha=1,facecolor='yellow',edgecolor='black',shadow=True,fancybox=True)
plt.show(block=True)