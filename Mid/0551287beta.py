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
		self.ovalwidth=[]
		self.ovalbg=[]
		self.ooval=[]
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
		for inputgraph in config.options('oval'):
			tmp=[]
			
			if inputgraph.find('range')!=-1:
				tmp=config['oval'][inputgraph].split(',')
				self.oval=(int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3]))
			
			elif inputgraph.find('width')!=-1:
				self.ovalwidth.append(int(config['oval'][inputgraph]))
				self.ooval.append(oval(self.oval[0],self.oval[1],self.oval[2],self.oval[3],self.ovalwidth[0],self.ovalbg[0]))
				self.oval=[]
				self.ovalwidth=[]
				self.ovalbg=[]
			elif inputgraph.find('outline')!=-1:
				self.ovalbg.append(config['oval'][inputgraph])
		self.linewidth=[]
		self.linefill=[]
		self.oline=[]
		for inputgraph in config.options('line'):
			tmp=[]
			if inputgraph.find('range')!=-1:
				tmp=config['line'][inputgraph].split(',')
				self.line=(int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3]))
			
			elif inputgraph.find('width')!=-1:
				self.linewidth.append(int(config['line'][inputgraph]))
				self.oline.append(line(self.line[0],self.line[1],self.line[2],self.line[3],self.linewidth[0],self.linefill[0]))
				self.line=[]
				self.linewidth=[]
				self.linefill=[]
			elif inputgraph.find('fill')!=-1:
				self.linefill.append(config['line'][inputgraph])
	def createtk(self):
		self.root=tk.Tk()
		self.root.title("期中考0551287")
		self.myfont=tkFont.Font(family='微軟正黑體',size=27,underline=True)
		self.label1text=tk.StringVar()
		self.label=tk.Label(self.root, textvariable=self.label1text)
		self.label1text.set('土木工程研究所碩士班')
		self.label.grid(row=1,column=1)
		self.lb1=tk.Listbox(self.root,width=8)
		self.lb1.insert(1,'Python')
		self.lb1.insert(2,'C++')
		self.lb1.insert(3,'C#')
		self.lb1.insert(4,'Java')
		self.lb1.grid(row=2,column=2)
		self.btn=tk.Button(self.root,text='按我',command=self.btnclick)
		self.btn.grid(row=3,column=3)
		self.root.mainloop()
	def btnclick(self):
		self.label1text.set(self.lb1.get(self.lb1.curselection()[0]))
		self.canvas = tk.Canvas(self.root,bg=self.bg,width=self.width, height=self.height)
		self.canvas.grid(row=4,column=1,columnspan=3)
		
		for nowoval in self.ooval:
			nowoval.drawoval(self.canvas)
		for nowline in self.oline:
			nowline.drawline(self.canvas)
		text('0551287張為舜',self.myfont).draw(self.canvas)

	#def drawit(self,t1)
	#	self.t1=t1

class text():
	def __init__(self,content,font):
		self.content=content
		self.font=font
	def draw(self,canvas):
		canvas.create_text(522,422,text=self.content,font=self.font)
class oval():
	def __init__(self,x0,y0,x1,y1,width,bg):
		self.x0=x0
		self.y0=y0
		self.x1=x1
		self.y1=y1
		self.width=width
		self.bg=bg
	def __str__(self):
		return "({0},{1},{2},{3})".format(self.x0,self.y0,self.x1,self.y1)
	def drawoval(self,canvas):
		print("drawoval")
		canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill = "yellow",width=self.width,outline=self.bg)
class line():
	def __init__(self,x0,y0,x1,y1,width,fill):
		self.x0=x0
		self.y0=y0
		self.x1=x1
		self.y1=y1
		self.width=width
		self.fill=fill
	def drawline(self,canvas):
		print("drawline")
		canvas.create_line(self.x0,self.y0,self.x1,self.y1,fill=self.fill,width=self.width)
	def __str__(self):
		return "({0},{1},{2},{3})".format(self.x0,self.y0,self.x1,self.y1)
def btnclick():
		self.label1text.set(self.lb1.get(self.lb1.curselection()[0]))
		self.canvas = tk.Canvas(self.root,bg=self.bg,width=self.width, height=self.height)
		self.canvas.grid(row=4,column=1,columnspan=3)
		
		for nowoval in self.ooval:
			nowoval.drawoval(self.canvas)
		for nowline in self.oline:
			nowline.drawline(self.canvas)
		text('0551287張為舜',self.myfont).draw(self.canvas)
def main():
	matrixfromini("0551287.ini").calreadfile()
	t1=draw("0551287.ini")
	
	t1.readfile()
	t1.createtk()
	t2=draw("0551287_2.ini")
	t2.readfile()
	#t2.drawit(t)

if __name__ == '__main__':
	main()