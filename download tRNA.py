from Bio import PDB
from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.MMCIFParser import MMCIFParser
pdb1 = PDB.PDBList()
pdb1.retrieve_pdb_file('1EHZ')
parser = MMCIFParser()
structure = parser.get_structure('1EHZ', '1ehz.cif')
for model in structure:
	for chain in model:
		print(chain)
		for  residue in chain:
			print(i, residue.resname, residue.id[1])
			for atom in residue:
					print(atom.name, atom.coord)
