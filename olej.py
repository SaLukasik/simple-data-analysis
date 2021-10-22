import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
from textwrap import wrap

A = np.loadtxt("654.txt")
x1=A[:,0]
print(x1)

x2=A[:,1]
print(x2)
x = np.linspace(-5,30,1)
l = 20.9
fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
dxx = [1,1,1,1,1,1,1,1,1,1]
dy = [2,2,2,2,2,2,2,2,2,2]
num_rows, num_cols = A.shape
plt.grid(True)

p = (0,1)
xxx= [0,25]

def g(xx,ff, bb):
    y =ff*xx + bb
    return y
par,cov = curve_fit(g,x1,x2,p0=p,sigma=dy,absolute_sigma=True)
plt.xlim([4, 25])
plt.ylim([7, 85])
ws = plt.errorbar(x1, x2, yerr=dy, xerr=dxx, fmt='.', color='red', label="punkty pomiarowe z naniesionym błędem")
print(par)
print(f'uwagagagagagagaga: {par[0]},,, {par[1]},,, niepewnosc:{np.sqrt(np.diag(cov))}')
plt.plot(xxx, g( np.asarray(xxx), 3.8484848484932432, -13.12727272730355), color ='blue', label="dopasowana krzywa")
print(par)
plt.xticks(np.arange(4, 26, 2.0))
plt.xlabel(r"h [mm]")
plt.ylabel(r"d [mm]")
plt.legend()
print(np.sqrt(np.diag(cov)))
'''
#fig.suptitle('Wykres zależności średniej odległości pudełek od osi optycznej od odległości pudełek od soczewki', fontsize=14, fontweight='bold')



'''

plt.savefig(r'olej.jpg')
k = 0
i = 0
n = 0
for k in range (0,num_rows):
    n += math.sqrt(1+(16*(A[k,0]**2)/A[k,1]**2))
k = 0
n = n/10
for k in range (0,num_rows):
    i += ((math.sqrt(1+(16*(A[k,0]**2)/A[k,1]**2))) - n)**2
i = i/10
k = i
k = np.sqrt(k)
i = 0
print(f'ODCHYLENIE STANDARDOWE: {k}')
'''for s in range (0,num_rows):
    i += ((y[s] - g(xx[s],par))/14.4)**2
    print(((y[s] - g(xx[s],par))/14.4)**2, y[s], g(xx[s],par))'''
k=0
n = 0
for k in range (0,num_rows):
    n += ((A[k,1] - g(A[k,0], 3.8484848484932432, -13.12727272730355))/(1))**2
k = 0
print(f'wartość CHi^2   {n}')

print(i)
print(2*i)
print("ooooo")
print(k)
print(i)
'''
print(cov)
print(np.sqrt(np.diag(cov)))
num_rows, num_cols = A.shape
i = 0
for s in range (0,num_rows):
    i += ((A[s,3] - g(A[s,0],*par))/0.1)**2

print(s)
k = (0.40848485/0.0215)
print(k)
n = k - 100/6


print(n)
print(1/n * 100)

c = 0.40848485
r = 0.0215090909
l = 6/100


x = np.sqrt(((l**2 *r)/(l*c-r))**2 * 0.01+ ((l**2 *c)/(l*c-r))**2 *0.0012 * + ((r**2)/(l*c-r))**2* 0.1)
print(x*100)
print(1/2.5 *100)
'''
