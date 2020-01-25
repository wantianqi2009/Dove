import linecache as li
import re
import os

#####主要用于检查vcrelax是否收敛
workdir2=os.getcwd()

def final(file):                     ###检测文件是否还有final字符
    b=1
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('final',line[i]):
                b=2
    return b

def exist(file):                     #####检测文件是否存在
    b=1
    if os.path.exists(file)==True:
        b=2
    return b


vclist=[]
a = os.listdir()
for i in a:
    if 'vc' in i:
        if os.path.isdir(i):
            vclist.append(i)


for p in vclist:
    workdir=workdir2+'/'+p+'/'+p+'.out'
    if exist(workdir) ==1:
        print(p+'didnt start')
    if exist(workdir) ==2:
        xxx=final(workdir)
        if xxx == 2:
            print(p+'has finished')
        if xxx == 1:
            print(p+'has not finished')

