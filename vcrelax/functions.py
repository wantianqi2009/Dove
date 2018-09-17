import linecache as li
import re
import numpy
import catch as ca

def cellparameters(file):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('Begin ', line[i]):
                b=i+4
    return b

def inputcellparameters(file):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall('CELL_PARAMETERS',line[i]):
                c=i
    return c

def nat(file):
    with open(file) as f:
        line= f.readlines()
        for i in range(0,len(line)):
            if re.findall('nat',line[i]):
                c=i
                count=line[i]
                a=count.split()
                b=a[2]
    return b

def ntype(file):
    with open(file) as f:
        line= f.readlines()
        for i in range(0,len(line)):
            if re.findall('ntyp',line[i]):
                c=i
                count=line[i]
                a=count.split()
                bbb=a[2]
    return bbb


def kp(file):
    with open(file) as f:
        line= f.readlines()
        for i in range(0,len(line)):
            if re.findall('K_POINTS',line[i]):
                count = line[i+1]
                x=count.split()
                a=int(x[0])
                b=int(x[1])
                c=int(x[2])
    return a,b,c

def pp(file):
    with open(file) as f:
        line= f.readlines()
        for i in range(0,len(line)):
            if re.findall('pseudo_dir',line[i]):
                c=i
    return c



def calculation(file):
    with open(file) as f:
        line=f.readlines()
        for i in range(0,len(line)):
            if re.findall('calculation', line[i]):
                c=i
    return c

def create_scfin(vcin,vcout,targetin):
    a=cellparameters(vcout)
    calline=calculation(vcin)
    numberat=int(nat(vcin))
    numbertype=int(ntype(vcin))
    b=inputcellparameters(vcin)
    ppdir=pp(vcin)
    with open(vcout) as vcsout:
        vc_out=vcsout.readlines()


    with open('vclocation') as hahaha:
        lineline=hahaha.readlines()
        scfkphangshu=ca.scfkp('vclocation')
    with open(vcin) as vcsin:
        line=vcsin.readlines()
        line[b-2]=lineline[scfkphangshu]+'\n'
        line[calline]='    calculation = "scf"\n'
        for n in range(b,b+4):
            line[n]=vc_out[a]
            a=a+1
        for x in range(b+7+numbertype,b+8+numbertype+numberat):
            line[x]=vc_out[a+1]
            a=a+1
        


    with open(targetin,'w') as scfin:
        for i in range(0,len(line)):
            scfin.write(line[i])
