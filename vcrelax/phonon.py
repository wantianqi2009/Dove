import functions as ca
import os
workdir=os.getcwd()
#with open('vclocation') as f:
#    line=f.readlines()
#    vcdir=line[1].strip()
vcdir=os.getcwd()
a=os.listdir(vcdir)

for i in range(0,len(a)):
    path=vcdir+'/'+a[i]
    if os.path.isdir(path):
        if 'vc' in a[i]:
            scfdir=str(a[i]).replace('vc','scf')
            if os.path.exists(scfdir) == False:
                os.mkdir(scfdir)
                target=workdir+'/'+scfdir+'/'+scfdir+'.in'
            else:
                target=workdir+'/'+scfdir+'/'+scfdir+'.in'

            b=os.listdir(vcdir+'/'+a[i])
            for x in range(0,len(b)):
                if 'in' in b[x]:
                    inp=vcdir+'/'+a[i]+'/'+b[x]
                if 'out' in b[x]:
                    out=vcdir+'/'+a[i]+'/'+b[x]
            ca.create_scfin(inp,out,target)


aa=os.listdir()
with open('ph.in') as ff:
    line = ff.readlines()

for ii in range(0,len(aa)):
    if 'scf' in aa[ii]:
        if 'job' in aa[ii]:
            print('1')
        else:
            scfdir=workdir+'/'+aa[ii]+'/'+aa[ii]+'.in'
            x,y,z=ca.kp(scfdir)
            phdir=workdir+'/'+aa[ii]+'/'+aa[ii]+'ph.in'
            with open(phdir,'w') as phinp:
                for xxx in range(0,len(line)-4):
                    phinp.write(line[xxx])
                phinp.write('nq1 = 2\n')
                phinp.write('nq2 = 2\n')
                phinp.write('nq3 = 2\n')
                phinp.write('/')

            

