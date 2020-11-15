##zip可以90°旋转表
##计算RNA序列的似然性
##复制
import os
multi=open("mutifasta.txt")
r_file=open("C:/Users/fangyu/Desktop/py/r_file.txt","w")
i=0
name=[]
index=[]
fasta=[]
for line in multi:
	i=i+1
	if line.startswith(">"):
		name.append(line.split("|")[1])
		index.append(i)
	elif not line.startswith(">"):
		if line.startswith("M") and i-1 in index:
			fasta.append(i-1)
a=0
for j in index:
	if j in fasta:
		print(name[a])
	a=a+1
##从选择的文本文件中删除偶数行
multi2=open("mutifasta2.txt")
k=0
deletefile=open("deletefile.txt","w")
for line in multi2:
	k+=1
	if k%2==0:
		continue
	else:
		deletefile.write(line)
##删除奇数行把0改成1就可以了
##在有相同行数的文件间寻找差异
s1=open("similarfasta1.txt")
s2=open("similarfasta2.txt")
s1_file=[]
s2_file=[]
for line in s1.readlines():
	s1_file.append(line.strip())

for line in s2.readlines():
	s2_file.append(line.strip())

for i in range(len(s1_file)):
   if s1_file[i]==s2_file[i]:
	   print("same")
   elif s1_file[i] not in s2_file:
	   print("uniq_s1")
   else:
	   print("uniq_s2")

##改进版：
for line1 in s1_file:
	if line1 not in s2_file:
		print(line1,"line unique in s1")
	else:
		print(line1,"also in s2")
for line2 in s2_file:
	if line2 not in s1_file:
		print(line2,"line unique in s2")
	else:
		print(line2,"also in s2")
##改进版
for line1 in s1_file:
	if line1 not in s2_file:
		print(">",line1,"line unique in s1")
	else:
		print("#",line1,"also in s2")
for line2 in s2_file:
	if line2 not in s1_file:
		print("<",line2,"line unique in s2")
	else:
		print("#",line2,"also in s2")
##转录本过滤器

rna1="AGXAUCUA"
rna2="ACCGUUCU"

		
		
