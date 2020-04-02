#class def
class Node:
	nodes=[]
	def __init__(self,arg1):
		self.neighbours=None
		self.letter=arg1
		Node.nodes.append(self)
	def get_neighbours(self,*n):
		self.neighbours=n
	def __repr__(self):
		return "Node with value "+self.letter
#--------------------------
#example graph creation
#nodes
for i in range(65,71):
	exec(chr(i)+'=Node("'+chr(i+32)+'")')
#connections
A.get_neighbours(B,D,E)
B.get_neighbours(A,C)
C.get_neighbours(B,E,F)
D.get_neighbours(A,E)
E.get_neighbours(A,C,D,F)
F.get_neighbours(E,C)
#----------------
#algorithm
def path(length):
	path.length=length
	def recur(s):
		path.depth+=1
		if path.depth==path.length:
			for n in s.neighbours:
				yield n
		else:
			for n in s.neighbours:
				for r in recur(n):
					yield [n,r]
		path.depth-=1
	for node in Node.nodes:
		path.depth=1
		for n in recur(node):
			yield [node,*n]
#----------------------
#test
for word in path(3):
	print(word)
#-----------------------
