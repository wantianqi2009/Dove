
import linecache as li
import re
def presee(file):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('press', line[i]):
            
                
                b=i
    return b

def pp(file):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('pseudo_dir',line[i]):
                c=i
    return c

def scfkp(file):
    with open(file) as f:
        line =f.readlines()
        for i in range(0,len(line)):
            if re.findall('scfnp',line[i]):
                c=i+1
    return c

def catchpress(file):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('Efinal',line[i]):
                c=i-7
                a=line[c].split()
                b=a[5]
                
    return b

def catchvolume(file):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('final unit-cell volume',line[i]):
                c=i
                a=line[c].split()
                b=a[4]
    return b

def catchenergy(file):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('Efinal',line[i]):
                c=i
                a=line[c].split()
                b=a[3]
    return b 
