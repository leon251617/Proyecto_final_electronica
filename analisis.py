import matplotlib.pyplot as plt
import numpy as np

Tem=np.loadtxt('312v.txt',unpack=True)
Tem1=np.loadtxt('303K.txt',unpack=True)
Tem2=np.loadtxt('321.txt',unpack=True)
Tem3=np.loadtxt('333.txt',unpack=True)
print(len(Tem3))
t=np.arange(1,1287,1)
t1=np.arange(1,1154,1)
t2=np.arange(1,1693,1)
t3=np.arange(1,2108,1)


########Filter codes
ft1=Tem1[400:1154:1]




######Statistics
m1=np.mean(ft1)
sig1=np.std(ft1)
print(m1)
print(sig1)

###PLOTS CODE
#plt.plot(t,Tem,'ro')
plt.plot(t1,Tem1,'bo')
#plt.plot(t2,Tem2,'go')
#plt.plot(t3,Tem3,'o',color='purple')
#plt.title("Temperatura en Funcion Del Tiempo Para 3.12V",fontsize=20)
#plt.xlabel("Tiempo  (s)",fontsize=20)
#plt.ylabel('Temperatura  ($^{o}C$)',fontsize=20)


#########Ploting means and standard deviation
plt.plot([0,1200],[26.5,26.5],'k--',lw=4)
plt.plot([0,1200],[26.5+0.682,26.5+0.682],'k--',lw=4)



plt.show()
