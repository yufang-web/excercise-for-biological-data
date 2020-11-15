##make an empty table
table=[[0]*6 for i in range(6)]
print(table)
##不能写成[row]*3简单重复三行，因为这样三行其实是同一行，改其中一行等于改所有。
##字典 用table[1]['ext2']访问字典 字典,当然可以给字典嵌套字典，让1变成一个键。比如row1是键，值是一个字典，包含一行四个变量的值
##单个列表转化为单个字典
table=[['protein','ext1','ext2','ext3'],
[0.16,0.038,0.044,0.040],
[0.33,0.089,0.095,0.091],
[0.66,0.184,0.191,0.191],
[1.00,0.280,0.292,0.283],
[1.32,0.365,0.367,0.365],
[1.66,0.441,0.443,0.444]
]
dic={}
n=0 ##外部字典键名序号
out_file=open("zhibiao.txt","w")
key=table[0]
for row in table[1:]: ##从第二行开始
    n=n+1
    entry={key[0]:row[0],key[1]:row[1],key[2]:row[2]} ##内部字典
    dic['row'+str(n)]=entry  #外部字典的值为内部字典
  
print(dic)

##转化为一个嵌套字典的列表
table1=[]
key=table[0]
for row in table[1:]:
	entry2={key[0]:row[0],key[1]:row[1],key[2]:row[2]}
	table1.append(entry2)
print(table1)
##添加平均消光列
table2=table
table2[0].append("mean")
p=0
for row in table[1:]:
	p=p+1
	mean=sum(row[1:])/3
	table2[p].append(round(mean,2))
print(table2)
##纯文本文件读取矩阵
RNAsimilar=open("RNAsimilar.txt")
j=0
key2=[]
data=[]
for line in RNAsimilar:
	j=j+1
	if j==1:
		key=line.strip().split("\t")
	else:
		key2.append(line.strip().split("\t")[0])
		data.append((line.strip().split("\t")[1:]))
print(data)   
l=0
table_test=[]
RNAsimilar=open("RNAsimilar.txt")
for line in RNAsimilar:
	table_test.append(line.strip().split("\t"))
print(table_test)
	                                     #for i in range(len(key)):
#	for j in range(len(key2)):
#	    inner_dic[key2[j-1]]=data[j-1][i-1]
#    RNA_dic[key[i-1]]=inner_dic
##计算rna序列的相似性
rna1="AGCAUCUA"
rna2="ACCGUUCU"
index1=0
index2=0
similarity=0
for base1,base2 in zip(rna1,rna2):
	if base1=="A":
		index1=1
	elif base1=="G":
		index1=2
	elif base1=="C":
		index1=3
	elif base1=="U":
		index1=4
	if base2=="A":
		index2=1
	elif base2=="G":
		index2=2
	elif base2=="C":
		index2=3
	elif base2=="U":
		index2=4
	similarity+=float(table_test[index1][index2])
print(similarity)
##选择性输出列和行
print(table[1])
for row in table:
	print(row[0])
for dic in table1:
	print(dic['protein'])
