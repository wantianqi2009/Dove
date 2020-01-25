from scipy.optimize import leastsq
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

volume=[]                                                  #####用catch.py 抓体积和能量
energy = []



volume = np.array(volume)*0.14818474347690475                #####体积默认为波尔的三次方，这里转化为埃的三次方
energy = np.array(energy)*13.605698066                       #####能量默认为ry，这里转化为电子伏特ev
def eos_birch_murnaghan(params, vol):
    ##'From Phys. Rev. B 70, 224107'
    E0, B0, Bp, V0 = params 
    E = E0+ (9*V0*B0/16)*(((V0/vol)**(2/3)-1)**3*Bp+((V0/vol)**(2/3)-1)**2*(6-4*(V0/vol)**(2/3)))
    return E

a, b, c = np.polyfit(volume, energy, 2)
V0 = -b/(2*a)
E0 = a*V0**2 + b*V0 + c
B0 = 2*a*V0
Bp = 4.0

x0 = [E0, B0, Bp, V0]

def print_params(label, params):
    E0, B0, Bp, V0 = params
    print(label, ": E0 = %f eV" % (E0))
    print(label, ": B0 = %f GPa" % (B0*160.21765))                    #####原来单位为电子伏特除以埃的三次方，这里转化为GPa
    print(label, ": Bp = %f" % (Bp))
    print(label, ": V0 = %f angstrom^3" % (V0))

target = lambda params, y, x: y - eos_birch_murnaghan(params, x)
birch_murn, ier = leastsq(target, x0, args=(energy,volume))
print_params("Birch-Murnaghan", birch_murn)

vfit = np.linspace(min(volume),max(volume),100)

plt.plot(volume,energy,'ro')
plt.plot(vfit,eos_birch_murnaghan(birch_murn,vfit),label='B-M')
plt.legend()
plt.savefig('1.pdf')


