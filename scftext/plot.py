import catch as ca
import os
import numpy as np
import catch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ecutwfc=[30,40,50,60,70,80,90,100,110,120,130,140]
kpoint=catch.kp2('kpoint')
number=[0,3,6,9,12,15,18,21,24,27,30,33]
x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[1,2,3,4,5,6,7,8,9,10,11]
energy1=[]
energy2=[]
energy3=[]
energy4=[]
workdir=os.getcwd()
os.chdir('%s/scfecut'%workdir)
for e in ecutwfc:
    a =ca.ce('%i.out'%e)
    b=float(a)
    energy1.append(b)
os.chdir('%s/scfkpoint'%workdir)
for k in number:
    c=ca.ce('%i.out'%k)
    d=float(c)
    energy2.append(d),print('%i.out'%k)
for m in range(0,len(energy1)-1):
    energy = float(energy1[m+1])-float(energy1[m])
    energy3.append(energy)
for mm in range(0,len(energy2)-1):
    ey = float(energy2[mm+1])-float(energy2[mm])
    energy4.append(ey)
os.chdir(workdir)
print(energy2)
plt.figure()
plt.plot(x,energy1,marker='o')
plt.xticks(x,ecutwfc)
plt.savefig('ecut.pdf')
plt.figure()
plt.plot(x,energy2,marker='o')
plt.xticks(x,kpoint)
plt.savefig('kpoint.pdf')
plt.figure()
plt.plot(y,energy3,c='b',marker='o')
plt.plot(y,energy4,c='r',marker='o')
plt.savefig('dif.pdf')

