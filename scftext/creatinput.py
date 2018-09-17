import re
import linecache as linecache
import os
import numpy as np
import catch
ecutwfc=[30,40,50,60,70,80,90,100,110,120,130,140]
kpoint=catch.kp('kpoint')
number = np.arange(0,len(kpoint)-2,3)
print(number)
workdir = os.getcwd()
pathtest1=os.path.exists('%s/scfecut'%workdir)
pathtest2= os.path.exists('%s/scfkpoint'%workdir)
aaa=catch.cdata('scf.in')
bbb=catch.cb('scf.in')
with open('scf.in') as f:
    line=f.readlines()
if pathtest1 == False:
    os.mkdir('%s/scfecut'%workdir)
if pathtest2 == False:
    os.mkdir('%s/scfkpoint'%workdir)
os.chdir('%s/scfecut'%workdir)
for n in ecutwfc:
    nn=4*n
    with open('%iecutscf.in'%n,'w') as h:
        for i in range(0,len(line)):
            if i == aaa:
                h.write('    ecutwfc     = %i\n'%n)
                h.write('    ecutrho     = %i\n'%nn)
            elif i ==aaa-1:
                print('%i done'%n)
            else:
                h.write(line[i])
os.chdir('%s/scfkpoint'%workdir)
for x in number:
    kp1=kpoint[x]
    kp2=kpoint[x+1]
    kp3=kpoint[x+2]
    print('%s %s %s done'%(kp1,kp2,kp3))
    with open('%ikpscf.in'%x,'w') as w:
        for ii in range(0,len(line)):
            if ii == bbb:
                w.write('%s  %s  %s  0 0 0\n'%(kp1,kp2,kp3))
            else:
                w.write(line[ii])
