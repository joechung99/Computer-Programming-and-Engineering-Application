import tkinter as tk
import tkinter.font as tkFont
import configparser
root=tk.Tk()
x=tk.StringVar()
label=tk.Label(root, textvariable=x)
label.grid(row=0,column=1)
edTxt=tk.Entry(root,width=10,borderwidth=5)
edTxt.insert(0,"test")
edTxt.grid(row=1,column=1)
canvasvaule=[]
ovalvalue=[]
linevalue=[]
myfont=tkFont.Font(family='標楷體',size=20)
class smile():
	def __init__(self,canvas,x,y):
		self.canvas=canvas
		self.x=int(x)
		self.y=int(y)
	def drawsmile(self):
		print("drawsmile")
		self.canvas.create_oval(self.x-50,self.y-50,self.x+50,self.y+50)
		self.canvas.create_oval(self.x-30,self.y-30,self.x-5,self.y-5)
		self.canvas.create_oval(self.x+5,self.y-30,self.x+30,self.y-5)
		self.canvas.create_arc(self.x-20,self.y-10,self.x+20,self.y+30,start=-120,extent=60,style="arc")
def readfile(inifile):
	matrix=[]
	'''canvasvaule=[]
	ovalvalue=[]
	linevalue=[]'''
	config = configparser.ConfigParser()
	config.read(inifile)
	matrix.append(config['data']['r1'].split(','))
	matrix.append(config['data']['r2'].split(','))
	matrix.append(config['data']['r3'].split(','))
	canvasvaule.append(config['graph']['width'])
	canvasvaule.append(config['graph']['height'])
	canvasvaule.append(config['graph']['bg'])
	ovalvalue.append(config['graph']['oval'].split(','))
	linevalue.append(config['graph']['line1'].split(','))
	linevalue.append(config['graph']['line2'].split(','))
	linevalue.append(config['graph']['line3'].split(','))
	return matrix
	#return matrix,canvasvaule,ovalvalue,linevalue

def matrixcal(matrix):
	aftermatrix=[[] * 2 for i in range(3)]
	for i in range(3):
		for j in range (3):
			tmp=0
			for k in range(3):
				tmp+=(int(matrix[i][k])*int(matrix[k][j]))
			
			aftermatrix[i].append(tmp)
	print("AxA:\n",aftermatrix[0])
	print(aftermatrix[1])
	print(aftermatrix[2])
def btnclick():
	x.set(edTxt.get())
	canvas = tk.Canvas(root,bg=canvasvaule[2],width=canvasvaule[0], height=canvasvaule[1])
	canvas.grid(row=2,column=3)
	#print("canvas print")
	canvas.create_line(linevalue[0][0],linevalue[0][1],linevalue[0][2],linevalue[0][3])
	canvas.create_line(linevalue[1][0],linevalue[1][1],linevalue[1][2],linevalue[1][3])
	canvas.create_line(linevalue[2][0],linevalue[2][1],linevalue[2][2],linevalue[2][3])
	canvas.create_oval(ovalvalue[0][0],ovalvalue[0][1],ovalvalue[0][2],ovalvalue[0][3],fill = "yellow")
	canvas.create_text(500,60,text='0551287張為舜',font=myfont)
	smile1=smile(canvas,300,300)
	smile1.drawsmile()
	smile2=smile(canvas,500,300)
	smile2.drawsmile()
def main():
	matrix=readfile("exam1.ini")
	#matrix,canvasvaule,ovalvalue,linevalue=readfile("exam1.ini")
	print("A=\n",matrix[0])
	print(matrix[1])
	print(matrix[2])
	matrixcal(matrix)
	root.title("小考")
	#root.geometry()
	x.set('土木工程學系')
	btn=tk.Button(root,text='按鈕物件',command=btnclick)
	btn.grid(row=1,column=2)
	root.mainloop()
	
if __name__ == '__main__':
	main()