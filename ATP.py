#calculate the △G#
from typing import Any
import math
ATP = [3.5 ,8.0, 2.6]
ADP = [1.8, 0.9, 1.7]
PI = [5.0, 8.0, 2.7]
R = 0.00831
T = 298
deltaG0 = -30.5
deltaG=[]
new: Any=0
for i in range(3):
    new = deltaG0+R*T*math.log(ADP[i]*PI[i]/ATP[i])
    deltaG.append(new)
print(deltaG)

#transfer#
print(len(deltaG))
deltaG_kcal=[]
new=0
for i in range(len(deltaG)):
	new=deltaG[i]/4.184
	deltaG_kcal.append(new)
print(deltaG_kcal)


#溶液质子浓度#
def pH_cal(ρ):
    pH=-math.log(ρ,10)
    return(pH)
print(pH_cal(0.003162))

#菌类指数增长#
def grow(n,t):
    grow_number=n*(2^(t*3))
    return(grow_number)
print(grow(1,6))

#VOLUME OF bacteria#
def volume(length,d):
	V=(d/2)**2*math.pi*length
	return(V)
print(volume(2.0,0.5))
#记录心得：关于这一次的自测题，首先是函数的封装，缩进，引用的package，变量的申明
#list可以用append添加新的元素，但是tuple里的定义了不可以改变。

