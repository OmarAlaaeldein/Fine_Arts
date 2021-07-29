from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import random as rn
import time
fig,ax=plt.subplots()
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
#x,y=symbols('x y')
#dispx1,dispy1,r1=int(input()),int(input()),int(input())
#dispx2,dispy2,r2=int(input()),int(input()),int(input())
#dispx3,dispy3,r3=int(input()),int(input()),int(input())
#C1=(x-dispx1)**2+(y-dispy1)**2-r1**2
#C2=(x-dispx2)**2+(y-dispy2)**2-r2**2
#C3=(x-dispx3)**2+(y-dispy3)**2-r3**2
#ex=C2-C1#-C3
#print(solve(ex))
col='bgrcykm'
d=np.linspace(-10,10,101)
for i in range(len(d)):
    ax.add_artist(plt.Circle((d[i],d[i]),d[i],fill=False,color=col[rn.randint(0,len(col)-1)]))
    ax.add_artist(plt.Circle((-d[i],-d[i]),d[i],fill=False,color=col[rn.randint(0,len(col)-1)]))
    ax.add_artist(plt.Circle((d[i],-d[i]),d[i],fill=False,color=col[rn.randint(0,len(col)-1)]))
    ax.add_artist(plt.Circle((-d[i],d[i]),d[i],fill=False,color=col[rn.randint(0,len(col)-1)]))
plt.show()