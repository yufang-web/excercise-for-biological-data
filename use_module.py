from neuron import DendrictLengths  ###put it under anaconda-lib-site packages workfold than we can use it xx.py  from xx import xx class
##then n can be an object of the module the data is the txt file
n = DendrictLengths('neuron_data.txt')
print(n)
print(n.get_average())
print(n.get_sttddev())
