import matplotlib.pyplot as plt

x=[0,1,2,3,4,5]
y=[i**2 for i in x]
plt.plot(x,y)
plt.title('Simple line plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show(block=True)
