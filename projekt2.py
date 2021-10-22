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
x = np.linspace(-5,20,1)
l = 20.9
fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
xx = [0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]
y = [0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]
num_rows, num_cols = A.shape
for s in range (0,num_rows):
    xx[s] = l - 2* x1[s]
    y[s] = 2*x2[s] -l
dxx = [0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2]
dy = [0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6]
p = (0)
xxx= [0,15]
print(xx)
print(y)
def g(xx,ff):
    y =ff*xx
    return y
par,cov = curve_fit(g,xx,y,p0=p,sigma=dy,absolute_sigma=True)
plt.xlim([0, 15])
plt.ylim([0, 15])
ws = plt.errorbar(xx, y, yerr=dy, xerr=dxx, fmt='.', color='red', label="punkty pomiarowe z naniesionym błędem")
print(par)
plt.plot(xxx, g(xxx, par), color ='blue', label="dopasowana krzywa")
print(par)


plt.xlabel(r"$l - 2x_{1} $ [cm]")
plt.ylabel(r"$2x_{2} - l $ [cm]")
plt.legend()
print(np.sqrt(np.diag(cov)))
'''
#fig.suptitle('Wykres zależności średniej odległości pudełek od osi optycznej od odległości pudełek od soczewki', fontsize=14, fontweight='bold')



'''
plt.savefig(r'zadanie2.jpg')
k = 0
i = 0
for k in range (0,num_rows):
    i += (A[k,1] - 14.14)**2
i = i/10
k = i
k = np.sqrt(k)
i = 0
for s in range (0,num_rows):
    i += ((y[s] - g(xx[s],par))/14.4)**2
    print(((y[s] - g(xx[s],par))/14.4)**2, y[s], g(xx[s],par))

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
