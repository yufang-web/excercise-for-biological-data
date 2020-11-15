#计算核苷酸序列碱基
insulin="GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT"
for amino_acid in "ACDEFGJIKLMNPQRSTVWY":
	number=insulin.count(amino_acid)
	print(amino_acid,number)

#分拆
number=insulin.count("A")
print("A",number)

#取字符
print(insulin[3])
print(insulin[-3])
#大小写


#创建随机序列
import random
alphabet="ACGT"  #范围序列
sequence=""  #随机序列
for i in range(10):   #长度
	index=random.randint(0, 3) #随机索引
	sequence=sequence+alphabet[index]
print (sequence)
#端粒蛋白质序列，DNA序列，一次一个残基输出氨基酸序列
i=1
n=0
while n<len(insulin):
	n=n+i
	print(insulin[n:n+i])
	i=i+1


#计算哪个氨基酸出现最频繁
insulin="GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT"
dic={}
for amino_acid in insulin:
	if amino_acid in dic:
		dic[amino_acid]+=1
	else:
		dic[amino_acid]=1
print(dic)
print(dic['G'])
index=0
max_value=dic[insulin[0]]
for i in range(len(insulin)):
	if dic[insulin[i]]>max_value:
		max_value=dic[insulin[i]]
		index=i+1
print(index,max_value)

#对字典进行排序


	
