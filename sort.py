from operator import itemgetter
####
data=[1,5,7,8,9,2,3,6,6,10]
data.reverse()
print(data)
###替换cmp
#operator.le(a, b)   
#operator.eq(a, b)   
#operator.ne(a, b)   
#operator.ge(a, b)   
#operator.gt(a, b)   
#operator.__lt__(a, b)   
#operator.__le__(a, b)   
#operator.__eq__(a, b)   
#operator.__ne__(a, b)   
#operator.__ge__(a, b)   
#operator.__gt__(a, b)
new_data=sorted(data)  #新变量
print(new_data)
###itemgetter‘ use
print(itemgetter(1)(data))
###倒序
new_data_reverse=sorted(data,reverse = True)
print(new_data_reverse)
##按长度对字符串进行排序，用lambda函数。
data=['ACCTGGCCA','ACTG','TACGGCAGGAGACG','TTGGATC']
bylenth=sorted(data,key=lambda x:len(x))
print("bylenth=",bylenth)
##对于数据表，可以用key表明自己相对哪一列数据进行排序——比如col:col[1]

##练习题
##按照第二列对表排序
lowry=open("lowry.txt")
new_file=open("new_file.txt","w")
lowry_list=[]
header=lowry.readline()
new_file.write(header)
for line in lowry:
	columns=line.split()
	columns=[float(x) for x in columns]
	lowry_list.append(columns)
print(lowry_list)     ####***不带引号方法，读入的时候
lowry_sort=sorted(lowry_list,key=itemgetter(1))
print(lowry_sort)
##已排序的前三列写入新文件
out2=''
i=0
for line in lowry_sort:
	i+=1
	if i<=3:    
		line1 = [str(x) for x in line]
		out2='\t'.join(line1) + '\n'
		new_file.write(out2)

###按照序列长度排序
multi_sort=open("mutifasta2.txt")
name=[]
fa=[]
i=0
l=0
for line in multi_sort:
	l+=1
	if line.startswith(">"):
		l=0
		i+=1
		fa.append([])
		name.append([])
		name[i-1].append(line.strip().split("|")[1])
	else:
		fa[i-1].append(line.strip())
print(len(fa))
fasta=[]
for i in range(len(fa)):
	fasta.append([])
	fasta[i].append("")
	for j in fa[i]:
		fasta[i][0]+=j
print(fasta) 
for i in range(len(fasta)):
	name[i].append(fasta[i][0])
	name[i].append(len(fasta[i][0]))
name_sort=sorted(name,key=itemgetter(2))
print(name_sort)
fasta_sort=open("fasta_sort.txt","w")
for lst in name_sort:
	lst=[str(x) for x in lst]
	out='\t'.join(lst)+'\n'
	fasta_sort.write(out)

##按照升序进行排序

