from main import Truss,Node
import tkinter as tk

class drawtruss():
	def __init__(self,truss,nodesize):
		self.truss=truss
		self.nodesize=nodesize

	def creatCanvas(self):
		self.root = tk.Tk()
		self.root.geometry("600x400")
		self.canvas = tk.Canvas(self.root,width=800, height=600)
		self.canvas.pack()

	def drawcircle(self):
		for i in self.truss.nodes:
			self.canvas.create_oval(self.fixpoint(i.x) - self.nodesize, self.fixpoint(i.y) - self.nodesize,self.fixpoint(i.x) + self.nodesize, self.fixpoint(i.y)  + self.nodesize, fill = "yellow")
			self.shapeLabel = self.canvas.create_text(self.fixpoint(i.x), self.fixpoint(i.y), text = i.name)

	def fixpoint(self,point):
		return(150+point)

	def drawbar(self):
		for i in self.truss.members:
			self.canvas.create_line((self.fixpoint(i.startnode.x), self.fixpoint(i.startnode.y), self.fixpoint(i.endnode.x), self.fixpoint(i.endnode.y)),width = i.area/5)
			self.canvas.create_text(self.fixpoint(i.startnode.x) + (self.fixpoint(i.endnode.x) - self.fixpoint(i.startnode.x))/1.5,self.fixpoint(i.startnode.y) + (self.fixpoint(i.endnode.y) - self.fixpoint(i.startnode.y))/1.5, font=("Helvetica", 10), text = i.name, fill="red")
