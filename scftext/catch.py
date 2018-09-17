
import linecache as li
import re
import sys
def cdata(file):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('ecutwfc', line[i]):
            
                count = li.getline(file,i+1)
                b=i
                li.clearcache()
                return b

def cb(file):
    with open(file) as ff:
        line = ff.readlines()
        for i in range(0,len(line)):
            if re.findall('K_POINTS',line[i]):
                b = i+1
                li.clearcache()
                return b

def ce(file):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('!    total energy',line[i]):
                count = li.getline(file,i+1)
                a=count.split()
                li.clearcache()
                b=a[4]
                return b

def kp(file):
    with open(file) as f:
        line=f.readlines()
        kpoint=[]
        if len(line) == 12:
            for i in range(0,len(line)):
                count=line[i]
                a=count.split()
                kpoint.extend(a)
            return kpoint
        else:
            print('You must have 12 kpoint')
            sys.exit(0)

def kp2(file):
    with open(file) as f:
        line = f.readlines()
        kpoint=[]
        for i in range(0,len(line)):
            count=line[i]
            a=count.split()
            b=str(a[0])+str(a[1])+str(a[2])
            kpoint.append(b)
        return kpoint




                
