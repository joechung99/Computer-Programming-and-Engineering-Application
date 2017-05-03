import numpy as np
import configparser
import math
def readfile(inifile):
	matrix=[]
	config = configparser.ConfigParser()
	config.read(inifile)
	for inputdata in config.options('data'):
		if inputdata.find('r')!=-1:
				matrix.append(config['data'][inputdata].split(','))
	npmatrix=np.array(matrix,dtype=float)
	ans=np.linalg.eig(npmatrix)
	print("A=\n",npmatrix)
	print("lambdal1=",ans[0][0])
	print("lambdal2=",ans[0][1])
	print("lambdal3=",ans[0][2])
	print("lambdal4=",ans[0][3])
	print(ans[1])
	npans=np.array(ans[1]).T
	config.set("solution",'lambdal1',str(ans[0][0]))
	config.set("solution",'lambdal2',str(ans[0][1]))
	config.set("solution",'lambdal3',str(ans[0][2]))
	config.set("solution",'lambdal4',str(ans[0][3]))
	config.set("solution",'vector1',str(npans[0]))
	config.set("solution",'vector2',str(npans[1]))
	config.set("solution",'vector3',str(npans[2]))
	config.set("solution",'vector4',str(npans[3]))
	config.write(open('ex0551287_1.ini', 'w'))
	
	
readfile("ex0551287_1.ini")