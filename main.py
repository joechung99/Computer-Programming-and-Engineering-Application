from draw import *
class Node:
	def __init__(self,x=0,y=0,name=""):
		self.x=x
		self.y=y
		self.name=name
		
class member:
	def __init__(self,startnode,endnode,name="",area=0):
		self.startnode=startnode
		self.endnode=endnode
		self.name=name
		self.area=area
		
	def memberlength(self):
		import math
		return(math.sqrt((self.startnode.x-self.endnode.x)**2+(self.startnode.y-self.endnode.y)**2))
	def membereal(self,e):
		return(float(e*self.area)/self.memberlength())
class Truss:
	nodes=[]
	members=[]
	def __init__(self, inifile):
		self.inifile=inifile
		
	def readini(self):
		import configparser
		try:
			config = configparser.ConfigParser()
			config.read(self.inifile)
			self.points=int(config['base']['points'])
			self.bars=int(config['base']['bars'])
			self.e=int(config['base']['e'])
			for inputnode in config.options('node'):
				if inputnode.find('p')!=-1:
					nodepoints=config['node'][inputnode].split(',')
					self.nodes.append(Node(int(nodepoints[0]),int(nodepoints[1]),inputnode))
					
			for inputmember in config.options('member'):
				if inputmember.find('bar')!=-1:
					barnodes=config['member'][inputmember].split(',')
					#print(barnodes)
					for i in self.nodes:
						for j in self.nodes:
							if i.name.strip('p')==barnodes[0] and j.name.strip('p')==barnodes[1]:
								self.members.append(member(i,j,inputmember))
					continue
				elif inputmember.find('area')!=-1:
					areanum=inputmember.strip('area')
					for n in self.members:
						if n.name.strip('bar')==areanum:
							n.area=float(config['member'][inputmember])
			#for n in self.nodes:
			#	print(n.name,n.x,n.y)
			#for n in self.members:
				#print(n.memberlength())
				#print(n.startnode, n.endnode, n.name,n.area)
		except:
			print("ini fail")
	def outputini(self):
		import configparser
		config = configparser.ConfigParser()
		f = open('0551287OUT.ini', 'w')
		config.add_section('MemberLengthResult')
		for i in self.members:
			config.set('MemberLengthResult',i.name," length %.1f,  E*A/L %.1f"%(i.memberlength(),i.membereal(self.e)))
		config.write(f)
		f.close()

def main():
	t=Truss("0551287.ini")
	t.readini()
	t.outputini()
	drawout=drawtruss(t,10)
	drawout.creatCanvas()
	drawout.drawbar()
	drawout.drawcircle()
	drawout.root.mainloop()
	
if __name__ == '__main__':
	main()