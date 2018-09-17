import catch
import linecache
import os
import re
import numpy as np
a=catch.presee('example.in')
workdir=os.getcwd()
aa=catch.presee('vclocation')
with open('vclocation') as ff:
    lineline = ff.readlines()
pressurelist=np.array(lineline[aa+1].split(), dtype=float)
with open('example.in') as f:
    line = f.readlines()
for p in pressurelist:
    test = os.path.exists('%s/vc%i'%(workdir,p))
    if test == False:
        os.mkdir('%s/vc%i'%(workdir,p))
    os.chdir('%s/vc%i'%(workdir,p))
    kbar = p*10
    with open('vc%i.in'%p,'w') as h:
        for n in range(0,len(line)):
            if n == a:
                h.write('press = %i\n'%kbar)
            else:
                h.write(line[n])
