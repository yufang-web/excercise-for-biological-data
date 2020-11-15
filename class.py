##创建一个类
##从类中创建对象
##让类可以打印
##为类创建一个单独的模块
##用方法执行类
class Pea:  ####类为p
    def __init__(self,genotype): 
        self.genotype=genotype
    def get_phenotype(self):
        if "G" in self.genotype:
            return "yellow"
        else:
            return "green"
    def create_offspring(self,other):
        offspring=[]
        new_genotype=""
        for haplo1 in self.genotype:
            for haplo2 in other.genotype:
                new_genotype=haplo1+haplo2
                offspring.append(Pea(new_genotype))
        return(offspring)
    def __repr__(self):
        return(self.get_phenotype()+'[%s]' % self.genotype)
yellow=Pea("GG")
green=Pea("gg")
f1=yellow.create_offspring(green)
f2=f1[0].create_offspring(f1[1])
print(f1)
print(f2)
