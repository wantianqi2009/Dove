import os
import re

def catchenergy(file):
    b = False
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('NOT',line[i]):
                b = True

    return b



a=os.listdir('./P21nm')
x=0
for n in a:
    heihei = catchenergy('./P21nm/%s/%s.out'%(n,n))
    if heihei == True:
        print('%s is not converge'%(n))
        x=x+1
print(x)
print(len(a))


b = os.listdir('./Pn21m')
for n in b:
    heihei = catchenergy('./Pn21m/%s/%s.out'%(n,n))
    if heihei == True:
        print('%s is not converge'%(n))