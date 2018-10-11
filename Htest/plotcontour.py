import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import catch

a1 = np.linspace(0.4,0.5,6)
a2 = np.linspace(0.5,0.6,6)



b1=np.linspace(0.4,0.6,12)
bb=0

noobczq = [[0 for i in range(12)] for j in range(6)]
for n in b1:
    aa=0
    for i in a1:
        i_idx=aa

        n_idx=bb

        noobczq[i_idx][n_idx] = float(catch.catchenergy('./P21nm/%f_%f21nm/%f_%f21nm.out'%(n,i,n,i)))
        aa=aa+1
    bb=bb+1

noobczq2 = [[0 for i in range(12)] for j in range(6)]
bb=0
for n in b1:
    aa=0
    for i in a2:
        i_idx=aa

        n_idx=bb

        noobczq2[i_idx][n_idx] = float(catch.catchenergy('./Pn21m/%f_%fn21m/%f_%fn21m.out'%(n,i,n,i)))
        aa=aa+1
    bb=bb+1


print(noobczq)
print(noobczq2)

x_grid,y_grid=np.meshgrid(b1,a1)
xx_grid,yy_grid=np.meshgrid(b1,a2)

#a = np.concatenate(a1, a2)


#plt.figure()
#plt.pcolor(x_grid, y_grid, noobczq, cmap='RdBu')
##plt.pcolor(xx_grid,yy_grid,noobczq2, cmap='RdBu')
#plt.colorbar(extend='both')
#plt.savefig('hahaha.png')

plt.subplot(2,1,1)
plt.pcolor(xx_grid,yy_grid,noobczq2, cmap='RdBu')
plt.colorbar(extend='both')
#plt.savefig('hahaha.png')

plt.subplot(2,1,2)
plt.pcolor(x_grid, y_grid, noobczq, cmap='RdBu')

plt.colorbar(extend='both')
#plt.savefig('hahaha.png')

plt.subplots_adjust(wspace =0, hspace =0)
plt.savefig('test.png')

