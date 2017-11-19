import matplotlib.pyplot as plt
import numpy as np

Tem=np.loadtxt('312v.txt',unpack=True)
Tem1=np.loadtxt('303K.txt',unpack=True)
Tem2=np.loadtxt('321.txt',unpack=True)
Tem3=np.loadtxt('333.txt',unpack=True)
Tem4=np.loadtxt('343.txt',unpack=True)
Tem5=np.loadtxt('363.txt',unpack=True)
#Tem6=np.loadtxt('383.txt',unpack=True)
print(len(Tem5))
t=np.arange(1,1287,1)
t1=np.arange(1,1154,1)
t2=np.arange(1,1693,1)
t3=np.arange(1,2108,1)
t4=np.arange(1,1884,1)
t5=np.arange(1,976,1)
########Filter codes
ft1=Tem1[400:1154:1]
ft=Tem[500:1287:1]
ft2=Tem2[600:1693:1]
ft3=Tem3[700:2108:1]
ft4=Tem4[1200:1884:1]
ft5=Tem5[300:975:1]

######Statistics
m1=np.mean(ft1)
sig1=np.std(ft1)

m=np.mean(ft)
sig=np.std(ft)

m2=np.mean(ft2)
sig2=np.std(ft2)


m3=np.mean(ft3)
sig3=np.std(ft3)

m4=np.mean(ft4)
sig4=np.std(ft4)


m5=np.mean(ft5)
sig5=np.std(ft5)


#m4=np.mean(ft4)
#sig4=np.std(ft4)

print(m5)
print(sig5)

###PLOTS CODE
plt.plot(t,Tem,'ro')
plt.plot(t1,Tem1,'bo')
plt.plot(t2,Tem2,'go')
plt.plot(t3,Tem3,'o',color='purple')
plt.plot(t4,Tem4,'o',color='cyan')
plt.plot(t5,Tem5,'o',color='orange')
#plt.title("Temperatura en Funcion Del Tiempo Para 3.12V",fontsize=20)
#plt.xlabel("Tiempo  (s)",fontsize=20)
#plt.ylabel('Temperatura  ($^{o}C$)',fontsize=20)


#########Ploting means and standard deviation
plt.plot([0,1400],[26.5,26.5],'k',lw=4)
plt.plot([0,1400],[26.5+0.682,26.5+0.682],'k--',lw=4)
plt.plot([0,1400],[26.5-0.682,26.5-0.682],'k--',lw=4)

plt.plot([0,1400],[m,m],'k',lw=4)
plt.plot([0,1400],[m+sig,m+sig],'k--',lw=4)
plt.plot([0,1400],[m-sig,m-sig],'k--',lw=4)


plt.plot([0,1400],[m2,m2],'k',lw=4)
plt.plot([0,1400],[m2+sig2,m2+sig2],'k--',lw=4)
plt.plot([0,1400],[m2-sig2,m2-sig2],'k--',lw=4)




plt.plot([0,1400],[m3,m3],'k',lw=4)
plt.plot([0,1400],[m3+sig3,m3+sig3],'k--',lw=4)
plt.plot([0,1400],[m3-sig3,m3-sig3],'k--',lw=4)


plt.plot([0,1600],[m4,m4],'k',lw=4)
plt.plot([0,1600],[m4+sig4,m4+sig4],'k--',lw=4)
plt.plot([0,1600],[m4-sig4,m4-sig4],'k--',lw=4)

plt.plot([0,1600],[m5,m5],'k',lw=4)
plt.plot([0,1600],[m5+sig5,m5+sig5],'k--',lw=4)
plt.plot([0,1600],[m5-sig5,m5-sig5],'k--',lw=4)
plt.show()
