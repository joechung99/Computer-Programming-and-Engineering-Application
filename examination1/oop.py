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
class draw():
	def __init__(self,inifile):
		self.inifile=inifile
	def readfile(self):
		config=configparser.ConfigParser()
		config.read(self.inifile)
		self.line=[]
		self.oval=[]
		for inputgraph in config.options('graph'):
			tmp=[]
			if inputgraph.find('width')!=-1:
				self.width=int(config['graph'][inputgraph])
				continue
			elif inputgraph.find('height')!=-1:
				self.height=int(config['graph'][inputgraph])
				continue
			elif inputgraph.find('bg')!=-1:
				self.bg=config['graph'][inputgraph]
				continue
			elif inputgraph.find('line')!=-1:
				tmp=config['graph'][inputgraph].split(',')
				self.line.append(line(int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3])))
				continue
			elif inputgraph.find('oval')!=-1:
				tmp=config['graph'][inputgraph].split(',')
				self.oval.append(oval(int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3])))
				continue
	def createtk(self):
		self.root=tk.Tk()
		self.myfont=tkFont.Font(family='標楷體',size=20)
		self.label1text=tk.StringVar()
		self.label=tk.Label(self.root, textvariable=self.label1text)
		self.label1text.set('土木工程學系')
		self.label.grid(row=0,column=1)
		self.edTxt=tk.Entry(self.root,width=10,borderwidth=5)
		self.edTxt.insert(0,"test")
		self.edTxt.grid(row=1,column=1)
		self.btn=tk.Button(self.root,text='按鈕物件',command=self.btnclick)
		self.btn.grid(row=1,column=2)
		self.root.mainloop()
	def btnclick(self):
		self.label1text.set(self.edTxt.get())
		self.canvas = tk.Canvas(self.root,bg=self.bg,width=self.width, height=self.height)
		self.canvas.grid(row=2,column=3)
		for nowline in self.line:
			nowline.drawline(self.canvas)
		for nowoval in self.oval:
			nowoval.drawoval(self.canvas)
		text('0551287張為舜',self.myfont).draw(self.canvas)
		smile1=smile(self.canvas,300,300)
		smile1.drawsmile()
		smile2=smile(self.canvas,500,300)
		smile2.drawsmile()
class smile():
	def __init__(self,canvas,x,y):
		self.canvas=canvas
		self.x=int(x)
		self.y=int(y)
	def drawsmile(self):
		self.canvas.create_oval(self.x-50,self.y-50,self.x+50,self.y+50)
		self.canvas.create_oval(self.x-30,self.y-30,self.x-5,self.y-5)
		self.canvas.create_oval(self.x+5,self.y-30,self.x+30,self.y-5)
		self.canvas.create_arc(self.x-20,self.y-10,self.x+20,self.y+30,start=-120,extent=60,style="arc")
class text():
	def __init__(self,content,font):
		self.content=content
		self.font=font
	def draw(self,canvas):
		canvas.create_text(500,60,text=self.content,font=self.font)
class oval():
	def __init__(self,x0,y0,x1,y1):
		self.x0=x0
		self.y0=y0
		self.x1=x1
		self.y1=y1
	def __str__(self):
		return "({0},{1},{2},{3})".format(self.x0,self.y0,self.x1,self.y1)
	def drawoval(self,canvas):
		canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill = "yellow")
class line():
	def __init__(self,x0,y0,x1,y1):
		self.x0=x0
		self.y0=y0
		self.x1=x1
		self.y1=y1
	def drawline(self,canvas):
		canvas.create_line(self.x0,self.y0,self.x1,self.y1)
	def __str__(self):
		return "({0},{1},{2},{3})".format(self.x0,self.y0,self.x1,self.y1)
		
def main():
	matrixfromini("exam1.ini").calreadfile()
	t=draw("exam1.ini")
	t.readfile()
	t.createtk()

if __name__ == '__main__':
	main()