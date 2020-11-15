import sys
class structure:
	def __init__(self,PDB_li,PDB_code,PDB_angle1,PDB_angle2):
		self.PDB_li=PDB_li
		self.PDB_code=PDB_code
		self.PDB_angle1=PDB_angle1
		self.PDB_angle2=PDB_angle2		
	def format_list(self):
		li = ''
		li = self.PDB_li + '\t' + self.PDB_code + '\t' + self.PDB_angle1 + '\t' + self.PDB_angle2	 + '\n'
		return li
	def __repr__(self):
		return self.format_list()
A=structure("A","a",'1','2')
print(A)
print(sys.path)
