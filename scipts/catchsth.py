import os
import re
def catch(file,keyword,linenumber,position):
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall(keyword,line[i]):
                c=i+int(linenumber)
                a=line[c].split()
                b=a[int(position)]
    return b

def catch2(file,keyword,linenumber,position):
    sssss=[]
    with open(file) as f:
        line = f.readlines()
        for i in range(0,len(line)):
            if re.findall(keyword,line[i]):
                c=i+int(linenumber)
                a=line[c].split()
                b=a[int(position)]
                sssss.append(b)
        sss=sssss[len(sssss)-2]
    return sss

vcdir=os.path.abspath(os.path.dirname(os.getcwd()))+'/vcrelax'
suibian=os.listdir(vcdir)
vcwjj=[]

volume=[]
energybfgsscf=[]
energybfgsvc=[]
for i in suibian:
    if 'vc' in i:
        if os.path.isdir(vcdir+'/'+i):
            vcwjj.append(i)


for ii in vcwjj:
    outfile=vcdir+'/'+ii+'/'+ii+'.out'
    ene=catch(outfile,'!',0,4)
    energybfgsscf.append(float(ene))                            ####这里取的能量是bfgs方法最后scf得出的能量
    vol=catch(outfile,'Final enthalpy',2,4)
    volume.append(float(vol))
    ene2=catch2(outfile,'!',0,4)
    energybfgsvc.append(float(ene2))

def out(shenme):
    if shenme == 'energybfgsscf':
        xxx=energybfgsscf
    if shenme == 'volume':
        xxx = volume
    if shenme == 'energybfgsvc':
        xxx = energybfgsvc
    return xxx

