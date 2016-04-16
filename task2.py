import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def d2Y_dt2(y, t, a, b):
    y0, y1 = y
    return np.array([a*(y0-y0*y1), b*(-y1+y0*y1)])
    
a = 1.0
b = 0.2
y0_initial = 0.1
y1_initial = 1.0
y_initial = [y0_initial, y1_initial]

t = np.linspace(0,5,100)
#solve ode 
solve = odeint(d2Y_dt2,y_initial,t,args=(a, b))

#Graph for Population against t
#y0 represent prey
#y1 represent predator
plt.plot(t, solve[:, 0], color='blue', label='y0(t)')
plt.plot(t, solve[:, 1], color='green', label='y1(t)')
plt.title('Graph Population against Time as y0(0)=0.1')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Population')
plt.grid()
plt.savefig('Graph_Population_against_Time_1.jpg')
plt.show()


#Graph for y1 against y0
plt.plot(solve[:, 0],solve[:,1], 'blue')
plt.title('Graph y1 against y0 as y0(0) = 0.1')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.savefig('Graph_y1_against_y0_1.jpg')
plt.show()

# Repeat the problem by changing y0(0)=0.11 and y1(0)=1.0 to compare the sensitivity
y_initial = [0.11, 1.0]
solve2 = odeint(d2Y_dt2,y_initial,t,args=(a, b))

#Graph for Population against t
plt.plot(t, solve2[:, 0], color='yellow', label='y0(t)')
plt.plot(t, solve2[:, 1], color='blue', label='y1(t)')
plt.title('Graph Population against Time as y0(0)=0.11')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Population')
plt.grid()
plt.savefig('Graph_Population_against_Time_2.jpg')
plt.show()

#Graph for y1 against y0
plt.plot(solve2[:, 0],solve2[:,1], 'yellow')
plt.title('Graph y1 against y0 as y0(0) = 0.11')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.savefig('Graph_y1_against_y0_2.jpg')
plt.show()