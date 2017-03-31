import tkinter as tk
import tkinter.font as tkFont
import configparser
import numpy
class matrixfromini():
	def __init__(self,inifile):
		self.inifile=inifile
	def calreadfile(self):
		matrix=[]
		config = configparser.ConfigParser()
		config.read(self.inifile)
		for inputdata in config.options('data'):
			if inputdata.find('r')!=-1:
				matrix.append(config['data'][inputdata].split(','))
		npmatrix=numpy.array(matrix,dtype=int)
		print("A=\n %s \n %s \n %s" %(matrix[0],matrix[1],matrix[2]))
		print("AxA=\n",npmatrix.dot(npmatrix))


def main():
	matrixfromini("exam1.ini").calreadfile()

if __name__ == '__main__':
	main()