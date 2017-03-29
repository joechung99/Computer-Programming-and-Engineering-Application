def readfile():
	import re
	f = open('0551287IN.txt','r')  
	node=list()
	bar=list()
	area=list()
	for line in f.readlines(): 
		line = line.strip() 
		line=re.split('=|,',line)
		if line[0].find('points')!=-1:
			nodenum=int(line[1])
			continue
		elif line[0].find('p')!=-1 and line[0]!='points':
			node.append(line)
			continue
		elif line[0].find('bars')!=-1:
			barsnum=int(line[1])
			continue
		elif line[0].find('bar')!=-1 and line[0]!='bars':
			bar.append(line)
			continue
		elif line[0].find('area')!=-1:
			area.append(line)
			continue
	return nodenum,node,barsnum,bar,area
def cal(nodenum,node,barsnum,bar,area):
	import math
	E=1000
	barlen=[[None] * 2 for i in range(barsnum)]
	for i in range(barsnum):
		tmp=list()
		head=int(bar[i][1])-1
		tail=int(bar[i][2])-1
		intbarlen=math.sqrt((int(node[head][1])-int(node[tail][1]))**2+(int(node[head][2])-int(node[tail][2]))**2)
		barlen[i][0]=intbarlen
		barlen[i][1]=E*int(area[i][1])/intbarlen
		#barlen[i].extend(area[i][1])/intbarlen)
		#tmp.append(intbarlen)
		#tmp.append(E*int(area[i][1])/intbarlen)
		#barlen.append(tmp)
	return barlen
def output(barlen,barsnum):
	f = open('0551287OUT.txt', 'w')
	for i in range(barsnum):
		f.write('bar%d的長度=%d E*A/L=%d\n' %(i+1,barlen[i][0],barlen[i][1]))
	print('output end')
def main():
	nodenum,node,barsnum,bar,area=readfile()
	barlen=cal(nodenum,node,barsnum,bar,area)
	output(barlen,barsnum)
if __name__ == '__main__':
	main()