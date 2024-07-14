from matplotlib import pyplot as plt
import math
x=[1,2,3,4,5,6]
y=[10,20,30,40,50,60]
y2=[20,40,60,80,100,120]
x1=[i**2 for i in x]


plt.suptitle("Sample")
plt.subplot(2,2,1)
plt.plot(x,y,marker='.',mfc='k',mec='k',c='yellow')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("X AND Y")
plt.subplot(2,2,2)
plt.plot(x,y2,marker='*',mfc='g',mec='g',c='red')
plt.title("X AND Y2")
plt.xlabel("Value of x")
plt.ylabel("Value of y2")
plt.subplot(2,2,3)
plt.plot(x1,y,marker='o',mfc='c',c='black')
plt.subplot(2,2,4)
plt.plot(x1,y2,marker='o',mfc='b',c='brown')
plt.show(block=True)
