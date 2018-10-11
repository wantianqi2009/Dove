import os
import re
import numpy as np
pathtest1 = os.path.exists('./P21nm')
pathtest2 = os.path.exists('./Pn21m')
if pathtest1 == False:
    os.mkdir('./P21nm')
if pathtest2 == False:
    os.mkdir('./Pn21m')








pn21mvc='./Pn21m.in'
p21nmvc='./P21nm.in'
with open(p21nmvc) as f1:
    line1 = f1.readlines()

with open(pn21mvc) as f2:
    line2 = f2.readlines()



line151=line1[51]
line152=line1[52]
line251=line2[51]
line252=line2[52]

Hn21dong=   line2[52].split()
On21dong =  line2[50].split()
On21dong2=  line2[48].split()
Hn21budong= line2[51].split()
On21budong =line2[49].split()
On21budong2=line2[47].split()


H21ndong=    line1[52].split()
O21ndong =   line1[50].split()
O21ndong2=   line1[48].split()
H21nbudong=  line1[51].split()
O21nbudong = line1[49].split()
O21nbudong2= line1[47].split()



###坐标1，3
nnn=[1,2]

####能动的那个H的grid
a1 = np.linspace(0.4,0.5,6)  #####P21nm
a2 = np.linspace(0.5,0.6,6)  #####pn21m

####不能动的那个H的grid
b1 = np.linspace(0.4,0.6,12)






####P21nm
for x1 in b1:
    for x2 in a1:
        pathtest = os.path.exists('./P21nm/%f_%f21nm'%(x1,x2))
        if pathtest == False:
            os.mkdir('./P21nm/%f_%f21nm'%(x1,x2))

###Pn21m
for xx1 in b1:
    for xx2 in a2:
        pathtesttest = os.path.exists('./Pn21m/%f_%fn21m'%(xx1,xx2))
        if pathtesttest == False:
            os.mkdir('./Pn21m/%f_%fn21m'%(xx1,xx2))


####P21nm
for n1 in b1:
    for n2 in a1:
        line1[51] = line151
        line1[52] = line152
        H1x=(float(O21nbudong[1])-float(O21nbudong2[1])) * n1 + float(O21nbudong2[1])
        H1xx = str('%.9f' % H1x)
        H1y=(float(O21nbudong2[2])-float(O21nbudong[2]))*(1-n1)+float(O21nbudong[2])
        H1yy = str('%.9f' % H1y)
        line1[51] = line1[51].replace(H21nbudong[1],H1xx)
        line1[51] = line1[51].replace(H21nbudong[2],H1yy)
        H2x=(float(O21ndong[1])+1-float(O21ndong2[1]))*n2+float(O21ndong2[1])
        k=H2x
        if k>1:
            k=k-1
        else:
            k=k
        H2xx=str('%.9f' %k)
        H2y=(float(O21ndong[2])-float(O21ndong2[2]))*n2+float(O21ndong2[2])
        H2yy=str('%.9f' %H2y)
        line1[52] = line1[52].replace(H21ndong[1],H2xx)
        line1[52] = line1[52].replace(H21ndong[2],H2yy)
        with open('./P21nm/%f_%f21nm/%f_%f21nm.in'%(n1,n2,n1,n2),'w') as writescf:
            for line in line1:
                writescf.write(line)


#        for i in nnn:
#            e=(float(O21nbudong[i])+float(O21nbudong2[i]))*n1
#            ee=str("%.9f" % e)
#            line1[51]=line1[51].replace(H21nbudong[i],ee)
#            f = (float(O21ndong[i])+ float(O21ndong2[i])) * n2
#            ff=str('%.9f' %f)
#            line1[52]=line1[52].replace(H21ndong[i],ff)
#
#            with open('./P21nm/%f_%f21nm/%f_%f21nm.in'%(n1,n2,n1,n2),'w') as writescf:
#                for line in line1:
#                    writescf.write(line)


        

for n1 in b1:
    for n2 in a2:
        line2[51] = line251
        line2[52] = line252
        H1x=(float(On21budong[1])-float(On21budong2[1])) * n1 + float(On21budong2[1])
        H1xx = str('%.9f' % H1x)
        H1y=(float(On21budong2[2])-float(On21budong[2]))*(1-n1)+float(On21budong[2])
        H1yy = str('%.9f' % H1y)
        line2[51] = line2[51].replace(Hn21budong[1],H1xx)
        line2[51] = line2[51].replace(Hn21budong[2],H1yy)
        H2x=(float(On21dong[1])+1-float(On21dong2[1]))*n2+float(On21dong2[1])
        k=H2x
        if k>1:
            k=k-1
        else:
            k=k
        H2xx=str('%.9f' %k)
        H2y=(float(On21dong[2])-float(On21dong2[2]))*n2+float(On21dong2[2])
        H2yy=str('%.9f' %H2y)
        line2[52] = line2[52].replace(Hn21dong[1],H2xx)
        line2[52] = line2[52].replace(Hn21dong[2],H2yy)
        with open('./Pn21m/%f_%fn21m/%f_%fn21m.in'%(n1,n2,n1,n2),'w') as writescf:
            for line in line2:
                writescf.write(line)
#        line2[51] = line251
#        line2[52] = line252
#        for i in nnn:
#            e = (float(On21budong[i]) + float(On21budong2[i])) * n1
#            ee=str('%.9f'%e)
#            line2[51]=line2[51].replace(Hn21budong[i],ee)
#            f = (float(On21dong[i])+ float(On21dong2[i])) * n2
#            ff=str('%.9f '%f)
#            line2[52]=line2[52].replace(Hn21dong[i],ff)
#
#            with open('./Pn21m/%f_%fn21m/%f_%fn21m.in'%(n1,n2,n1,n2),'w') as writescf:
#                for line in line2:
#                    writescf.write(line)