import numpy as np
import configparser
import math
import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)
def func(t,u,P,K,C,M):
	return [u[1],(P-K*u[0]-C*u[1])/M]
def readfile(inifile):
	config = configparser.ConfigParser()
	config.read(inifile)
	M=int(config['data']['m'])
	C=int(config['data']['c'])
	K=int(config['data']['k'])
	P=int(config['data']['p'])
	inity=int(config['data']['inity'])
	initv=int(config['data']['initv'])
	u=[inity,initv]
	dt=0.01
	sec=100
	wn=math.sqrt(K/M)
	fn=wn/(2*math.pi)
	X=[]
	Y=[]
	plt.title("%.2f*y''+%.2f*y'+%.2f*y=0 y(0)=%d y'(0)=%d" %(M,C,K,u[0],u[1]))
	for i in range(int(sec/dt)):
		t=i*dt
		X.append(t)
		Y.append(u[0])
		tM=t+dt/2
		k1=func(t,u,P,K,C,M)
		uM=[u[0]+dt/2*k1[0],u[1]+dt/2*k1[1]]
		k2=func(tM,uM,P,K,C,M)
		uM=[u[0]+dt/2*k2[0],u[1]+dt/2*k2[1]]
		k3=func(tM,uM,P,K,C,M)
		u1=[u[0]+dt*k3[0],u[1]+dt*k3[1]]
		k4=func(t+dt,u1,P,K,C,M)
		u=[u[0]+dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]),
			u[1]+dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])]
		config.set("solution",'y'+str(i),str(u[0]))
		#print(i,u[0])
	config.write(open('ex0551287_2.ini', 'w'))
	print("fn:=%f Hz      T=%f\n"% (fn,1/fn))
	plt.xlabel('t')
	plt.ylabel('y')
	plt.plot(X,Y)
	plt.show
readfile("ex0551287_2.ini")