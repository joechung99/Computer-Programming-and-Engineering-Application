class Node:
	def __init__(self,x=0,y=0,name=""):
		self.x=x
		self.y=y
		self.name=name
def readfile():
	import configparser
	try:
		config = configparser.ConfigParser()
		config.read("test.ini")
		points=int(config['base']['points'])
		bars=int(config['base']['bars'])
		e=int(config['base']['e'])
		for i in config.options('node'):
			nodepoints=config['node'][i].split(',')
			#i=class Node(,,i)
			print (nodepoints)
	except:
            print("ini fail")
def main():
	readfile()

if __name__ == '__main__':
	main()