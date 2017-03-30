import tkinter as tk
import configparser
root=tk.Tk()

x=tk.StringVar()
label=tk.Label(root, textvariable=x)
label.grid(row=0,column=1)
edTxt=tk.Entry(root,width=10,borderwidth=5)
edTxt.grid(row=1,column=1)
def readfile(inifile):
	matrix=[]
	config = configparser.ConfigParser()
	config.read(inifile)
	matrix.append(config['data']['r1'].split(','))
	matrix.append(config['data']['r2'].split(','))
	matrix.append(config['data']['r3'].split(','))
	return matrix

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
	canvas = tk.Canvas(root,width=800, height=600)
	canvas.create_line(1,1,2,2,width=5)
def main():
	matrix=readfile("exam1.ini")
	print("A=\n",matrix[0])
	print(matrix[1])
	print(matrix[2])
	matrixcal(matrix)
	#root=tk.Tk()
	root.title("小考")
	root.geometry("400x400")
	#x=tk.StringVar()
	x.set('土木工程學系')
	#label=tk.Label(root, textvariable=x)
	#label.grid(row=3,column=0,rowspan=2)
	#edTxt=tk.Entry(root,width=10,borderwidth=5)
	#edTxt.grid(row=3,column=2)

	btn=tk.Button(root,text='按鈕物件',command=btnclick)
	btn.grid(row=1,column=2)
	root.mainloop()
	
if __name__ == '__main__':
	main()