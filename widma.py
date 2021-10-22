import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
import math
from uncertainties import ufloat
from uncertainties.umath import *
import random
from scipy.optimize import curve_fit
from statistics import mean
print("~")

W = [320+9/60-50-22/60, 324+10/60-54-23/60,319+51/60-50-0/60,317+51/60-47-53/60,323-53+40/60-49/60]

for t in range (0,len(W)):
    W[t] = 1/2*(360 - W[t])
    print(W[t])

print(np.mean(W))
print(np.std(W))
dziel = ufloat(45+4/60+37/360,18/360)
''' T = [ufloat(+/60,1/20),ufloat(+/60,1/20),ufloat(+/60,1/20),ufloat(+/60,1/20),ufloat(+/60,1/20)]  '''
A = [ufloat(37+15/60,1/20),ufloat(37+10/60,1/20),ufloat(37+15/60,1/20),ufloat(37+17/60,1/20),ufloat(37+14/60,1/20)]
B= [ufloat(322+46/60,1/20),ufloat(322+45/60,1/20),ufloat(322+45/60,1/20),ufloat(322+40/60,1/20),ufloat(322+47/60,1/20)]
A=[ufloat(36+47/60,1/20),ufloat(36+45/60,1/20),ufloat(36+38/60,1/20),ufloat(36+39/60,1/20),ufloat(36+42/60,1/20)]
B = [ufloat(323+18/60,1/20),ufloat(323+18/60,1/20),ufloat(323+23/60,1/20),ufloat(323+17/60,1/20),ufloat(323+23/60,1/20)]
A=[ufloat(36+18/60,1/20),ufloat(36+17/60,1/20),ufloat(36+30/60,1/20),ufloat(36+17/60,1/20),ufloat(36+15/60,1/20)]
B = [ufloat(323+44/60,1/20),ufloat(323+47/60,1/20),ufloat(323+47/60,1/20),ufloat(323+43/60,1/20),ufloat(323+42/60,1/20)]
A = [ufloat(36+36/60,1/20),ufloat(36+31/60,1/20),ufloat(36+35/60,1/20),ufloat(36+32/60,1/20),ufloat(36+39/60,1/20)]
B = [ufloat(323+31/60,1/20),ufloat(323+33/60,1/20),ufloat(323+31/60,1/20),ufloat(323+32/60,1/20),ufloat(323+31/60,1/20)]
A=[ufloat(35+32/60,1/20),ufloat(35+32/60,1/20),ufloat(35+33/60,1/20),ufloat(35+33/60,1/20),ufloat(35+34/60,1/20)]
B=[ufloat(324+25/60,1/20),ufloat(324+25/60,1/20),ufloat(324+25/60,1/20),ufloat(324+27/60,1/20),ufloat(324+28/60,1/20)]
A=[ufloat(36+58/60,1/20),ufloat(36+59/60,1/20),ufloat(37+11/60,1/20),ufloat(37+0/60,1/20),ufloat(37+2/60,1/20)]
B= [ufloat(322+59/60,1/20),ufloat(322+56/60,1/20),ufloat(322+48/60,1/20),ufloat(322+56/60,1/20),ufloat(322+59/60,1/20)]
A=[ufloat(35+10/60,1/20),ufloat(35+10/60,1/20),ufloat(35+10/60,1/20),ufloat(35+7/60,1/20),ufloat(35+12/60,1/20)]
B=[ufloat(342+49/60,1/20),ufloat(324+56/60,1/20),ufloat(324+55/60,1/20),ufloat(324+55/60,1/20),ufloat(324+52/60,1/20)]

A=[ufloat(35+10/60,1/20),ufloat(35+8/60,1/20),ufloat(35+12/60,1/20),ufloat(35+11/60,1/20),ufloat(35+10/60,1/20)]
B=[ufloat(324+49/60,1/20),ufloat(324+45/60,1/20),ufloat(324+50/60,1/20),ufloat(324+43/60,1/20),ufloat(324+50/60,1/20)]

A=[ufloat(36+28/60,1/20),ufloat(36+29/60,1/20),ufloat(36+26/60,1/20),ufloat(36+31/60,1/20),ufloat(36+28/60,1/20)]
B=[ufloat(323+33/60,1/20),ufloat(323+30/60,1/20),ufloat(323+31/60,1/20),ufloat(323+34/60,1/20),ufloat(323+35/60,1/20)]

A=[ufloat(35+38/60,1/20),ufloat(35+37/60,1/20),ufloat(35+32/60,1/20),ufloat(35+31/60,1/20),ufloat(35+33/60,1/20)]
B= [ufloat(324+29/60,1/20),ufloat(324+28/60,1/20),ufloat(324+33/60,1/20),ufloat(324+32/60,1/20),ufloat(324+28/60,1/20)]

A = [ufloat(37+15/60,5/60),ufloat(37+10/60,5/60),ufloat(37+15/60,5/60),ufloat(37+17/60,5/60),ufloat(37+14/60,5/60)]
B = [ufloat(322+46/60,5/60),ufloat(322+45/60,5/60),ufloat(322+45/60,5/60),ufloat(322+40/60,5/60),ufloat(322+47/60,5/60)]

A = [ufloat(36+47/60,5/60),ufloat(36+45/60,5/60),ufloat(36+38/60,5/60),ufloat(36+39/60,5/60),ufloat(36+42/60,5/60)]
B = [ufloat(323+18/60,5/60),ufloat(323+18/60,5/60),ufloat(323+23/60,5/60),ufloat(323+17/60,5/60),ufloat(323+23/60,5/60)]


delmin = [0,0,0,0,0]
for t in range (0,len(delmin)):
    delmin[t] = 1/2*(360 -B[t]+ A[t])
    print(delmin[t])
s = 0
for t in range (0,len(delmin)):
    s += delmin[t]

print("ooo")
s = s/len(delmin)
print(s)
s = 2*3.1415926535879*s/360
n = (sin(1/2*(s+dziel)))/(sin(1/2*dziel))
print("***")
print(n)
print("startujemy z dopasowywaniem")



t= [434.05**2,447.15**2,471.31**2,486.13**2,492.19**2,501.57**2,587.56**2,656.28**2,667.81**2]
n = [1.421,1.419,1.416,1.414,1.413,1.412,1.405,1.401,1.383]
dn = [0.026,0.025,0.025,0.025,0.025,0.025,0.024,0.024,0.023]
n2 = [1.421**2,1.419**2,1.416**2,1.414**2,1.413**2,1.412**2,1.405**2,1.401**2,1.383**2]
dn2 = [0.026*2,0.025*2,0.025*2,0.025*2,0.025*2,0.025*2,0.024*2,0.024*2,0.023*2]
plt.errorbar(t, n, yerr=dn, linestyle='None', marker='.',color='red', label="punkty pomiarowe z naniesionym błędem")
def objective(x, a,b):
	return a + b/x
popt, cov = curve_fit(objective, t, n, sigma=dn,absolute_sigma=True)
print(f"Swidnwidneifenifef::::{popt}, {np.sqrt(np.diag(cov))} ")
x_fit = np.linspace(t[0],t[8], 10000)
y_fit = objective(x_fit, *popt)

plt.plot(x_fit, y_fit, color ='blue', label="dopasowana krzywa")
plt.xlabel(r"$\omega$ [nm$^2$]")
plt.ylabel(r"$n$")
plt.legend()
plt.grid(True)
plt.savefig(r'widma1.jpg')
def objective2(x, b,c):
    return (b*x)/(x-c)+1
popt, cov = curve_fit(objective, t, n2, sigma=dn2,absolute_sigma=True)
print(f"Swidnwidneifenifef::::{popt}, {np.sqrt(np.diag(cov))} ")
plt.figure(66666)
plt.errorbar(t, n2, yerr=dn2, linestyle='None', marker='.',color='red', label="punkty pomiarowe z naniesionym błędem")
x_fit = np.linspace(t[0],t[8], 10000)
y_fit = objective(x_fit, *popt)
plt.grid(True)
plt.plot(x_fit, y_fit, color ='blue', label="dopasowana krzywa")
plt.xlabel(r"$\omega$ [nm$^2$]")
plt.ylabel(r"$\xi$")
plt.legend()
plt.savefig(r'widma2.jpg')
plt.show()
n = ufloat(1.416,0.024)
A1 = ufloat(9748.16,7721.89)
A0 = ufloat(1.37,0.03)
B1 = ufloat(1.88,0.06)
C1 = ufloat(27378.32,15443.81)

print("<3<3<3")
print(sqrt((A1)/(n-A0)))
print(sqrt(((n*n-1)*C1)/-(n*n - 1 - B1)))
