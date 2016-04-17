import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def dy_dt(y,t):
    a=1.0
    b=0.2
    return [a*(y[0]-y[0]*y[1]),b*(-y[1]+y[0]*y[1])]

#initialize intial condition
y=[0.1,1.0]
t=np.linspace(0,5,200)
Y=sp.integrate.odeint(dy_dt,y,t)

ax1=plt.figure().add_subplot(211)
ax1.plot(t, Y)
plt.xlabel("Time/t")
plt.ylabel("Prey_Predator_y ");
plt.plot(t, Y[:,0], label='prey', color="red")
plt.plot(t, Y[:,1], label='predator', color="green")
plt.title('Prey_Predator vs Time')
plt.grid()

ax2=plt.figure().add_subplot(212)
ax2.plot(Y[:,0], Y[:,1])
plt.xlabel("Prey_y0")
plt.ylabel("Predator_y1 ");
plt.title(' Predator vs Prey')
plt.grid()

### change initial to test sensitivity on inutial

y_new=np.array([0.11,1.0])                 
t=np.linspace(0, 5, 200)
Y_new= sp.integrate.odeint(dy_dt,y_new,t)


ax3=plt.figure().add_subplot(211)
ax3.plot(t, Y_new)
plt.xlabel("Time/t")
plt.ylabel("Prey_Predator_Y ");
plt.plot(t, Y_new[:,0], label='prey', color="red")
plt.plot(t, Y_new[:,1], label='predator', color="green")
plt.title('Prey_Predator_Y_New vs Time')
plt.grid()

ax4=plt.figure().add_subplot(212)
ax4.plot(Y_new[:,0], Y_new[:,1])
plt.xlabel("Prey_y0")
plt.ylabel("Predator_Y1 ");
plt.title(' Predator vs Prey Y_New')
plt.grid()

yy=[Y,Y_new]
ax1.plot(t, Y_new ,t, Y)