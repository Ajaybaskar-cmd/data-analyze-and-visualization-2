from matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,11)
y=x*10
print(x,y)
f1={'family':'calibri','size':35,'color':'red'}
f2={'family':'cambria','size':25,'color':'yellow'}
plt.plot(x,y,marker='.',ls='dotted')
plt.title('Example of Font properties',fontdict=f1)
plt.xlabel("X-values",fontdict=f2)
plt.ylabel("Y-values",fontdict=f2)
plt.show(block=True)