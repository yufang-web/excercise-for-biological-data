##读取和写入文件、就算平均值和标准差
neuron_data=open('neuron_data.txt')
data=[]
for line in neuron_data:
	print(line)
	length=float(line.strip()) #从文本读取的是字符串要转化为数字
	data.append(length)
print(data)
sum_data=sum(data)
mean_data=sum_data/len(data)
max_data=max(data)
min_data=min(data)
print(sum_data,mean_data,max_data,min_data)
s_p=0
for value in data:
	s_p=s_p+float((value-mean_data)**2)/float(len(data))  #使用pow（a,b）或者a**b，^在python里是逻辑运算符
s=s_p**0.5  #cmath.sqrt
print('s=',s)
#读fasta文件
import re
fasta=open('ffile.fasta')
A_sum=0
T_sum=0
C_sum=0
G_sum=0
A=0
T=0
G=0
C=0
for line in fasta:
	if line.startswith(">"):
		continue
	else:
		A=len(re.findall("A",line))  #返回关键词搜索结果。务必要记住，continue跳出本次循环，break跳出整个循环。注意要IMPORT RE
		T=len(re.findall("T",line))
		C=len(re.findall("C",line))
		G=len(re.findall("G",line))
		A_sum+=A
		T_sum+=T
		C_sum+=C
		G_sum+=G
sum_base=[A_sum,T_sum,C_sum,G_sum]
p_base=max(sum_base)/sum(sum_base)
print(p_base) #如果具体要知道是哪个碱基可能要用到循环。
print(A_sum,T_sum,C_sum,G_sum)
##GC含量
print((G_sum+C_sum)/sum(sum_base))

##创建一个字典
dict={'UAA':'Stop','UAG':'Stop','UGA':'Stop','AUG':'Start','GGG':'Glycin'}

##对起始和终止密码子进行计数
rna=open("rnafile.fasta")
RNA=''
for line in rna:
	if not line.startswith(">"):
		RNA=RNA+line.strip()
print(RNA)
RNA1=RNA.replace('T','U')
print(RNA1)
#第一个循环用来把RNA合并为一个字符串
#替换可以使用字符换，也可以指定最大替换数量
##使用偏好表，写一个基于序列的二级结构元素预测的程序.20
pref_H={'A':1.45,'C':0.77,'D':0.98,'E':1.53,'F':1.12,'G':0.53,'H':1.24,'I':1.00,'K':1.07,'L':1.34,'M':1.20,'N':0.73,'P':0.59,'Q':1.17,'R':0.79,'S':0.79,'T':0.82,'V':1.14,'W':1.14,'Y':0.61}
pref_E={'A':0.97,'C':1.30,'D':0.80,'E':0.26,'F':1.28,'G':0.81,'H':0.71,'I':1.60,'K':0.74,'L':1.22,'M':1.67,'N':0.65,'P':0.62,'Q':1.23,'R':0.90,'S':0.72,'T':1.20,'V':1.65,'W':1.19,'Y':1.29}
protein="AHSKLMEFFFTVW" ##序列
protein_predict=""
for i in range(len(protein)):
	value=protein[i]
	if pref_H[value]>=1 and pref_E[value]<pref_H[value]:
		protein_predict+="H"
	elif pref_E[value]>=1 and pref_E[value]>pref_H[value]:
		protein_predict+="E"
	else:
		protein_predict+="L"
print(protein_predict)
##编写蛋白质序列中氨基酸残基溶剂可及性的预测程序
protein_file=open("proteinfile.fasta")
protein2=""
output=""
SEA={'A':0.48,'C':0.32,'D':0.81,'E':0.93,'F':0.42,'G':0.51,'H':0.66,'I':0.39,'K':0.93,'L':0.41,'M':0.44,'N':0.82,'P':0.78,'Q':0.81,'R':0.84,'S':0.70,'T':0.71,'V':0.40,'W':0.49,'Y':0.67}
for line in protein_file:
	if not line.startswith(">"):
		protein2+=line.strip()
print(protein2)
for base in protein2:
	if SEA[base]>0.7:
		output+=base.upper()
	else:
		output+=base.lower()
print(output)
