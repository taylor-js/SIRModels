import scipy.integrate as spi
import numpy as np
import pylab as pl

mu=1/(70*365.0)
beta=520/365.0
sigma=1/14.0
gamma=1/7.0
ND=60*365.0
TS=1.0
S0=0.1
E0=1e-4
I0=1e-4
INPUT = (S0, E0, I0)

def SEIR(x,t):  
	'''The main set of equations'''
	Y=np.zeros((3))
	X = x    
	Y[0] = mu - beta * X[0] * X[2] - mu * X[0]
	Y[1] = beta * X[0] * X[2] - sigma * X[1] - mu * X[1]
	Y[2] = sigma * X[1] - gamma * X[2] - mu * X[2]
	return Y   # For odeint



t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)

Rec=1. - (RES[:,0]+RES[:,1]+RES[:,2])
print(RES)

#Ploting
pl.subplot(311)
pl.plot(RES[:,0], '-g', label='Susceptibles')
pl.title('Program_2_6.py')
pl.xlabel('Time')
pl.ylabel('Susceptibles')
pl.subplot(312)
pl.plot(RES[:,1], '-m', label='Exposed')
pl.plot(RES[:,2], '-r', label='Infectious')
pl.legend(loc=0)
pl.xlabel('Time')
pl.ylabel('Infected')
pl.subplot(313)
pl.plot(Rec, '-k', label='Recovereds')
pl.xlabel('Time')
pl.ylabel('Recovereds')
pl.show()