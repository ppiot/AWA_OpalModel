from opal.opal import load_dataset
import matplotlib.pyplot as plt
import numpy as np 

rootname='awaDrive2YAG1'
stat = load_dataset('./', fname=rootname+'.stat')
print (stat)
coord = load_dataset('./', fname=rootname+'.h5')
print (coord)
#plt = stat.plot_envelope()

#for i in range(40)

Bcath=stat.getData('Bz_ref')
x=stat.getData('Bz_ref')
#print(coord.getRow('x'))
#plt = coord.plot_phase_space('x', 'z', xsci=True, ysci=True, step=93)

SPOS=coord.getData('SPOS')
 
for i in range(len(SPOS)):
   if i==0:
      x=coord.getData('x', step=i)
      z=SPOS[i]+coord.getData('z', step=i)
   if i>0:
      x=np.append(x,coord.getData('x', step=i))
      z=np.append(z,SPOS[i]+coord.getData('z', step=i))
print (coord.getData('SPOS'))
print (i)
#plt.plot (z,x,'.')
plt = coord.plot_density('x', 'z', xsci=True, ysci=True, step=i, bins=21)
plt.figure()
plt = coord.plot_density('y', 'z', xsci=True, ysci=True, step=i, bins=21)
plt.show()


