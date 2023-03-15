#!/usr/bin/python

import math;
import numpy as np
from linmach import linmach
from confus import confus
from perceptron import perceptron

data=np.loadtxt('expressions');
N,L=data.shape; 
D=L-1;
labs=np.unique(data[:,L-1]); 
C=labs.size;

np.random.seed(23); 
perm=np.random.permutation(N);
data=data[perm];

NTr=int(round(.7*N));
train=data[:NTr,:];
M=N-NTr;
test=data[NTr:,:];

print('#     a   E   k  Ete');
print('#------- --- --- ---');

for a in [.1,1,10,100,1000,10000,100000]:
  w,E,k=perceptron(train,a=a, K=200);
  rl=np.zeros((M,1));
  for m in range(M):
     tem=np.concatenate(([1],test[m,:D]));
     rl[m]=labs[linmach(w,tem)];
  nerr,m=confus(test[:,L-1].reshape(M,1),rl);
  print('%8.1f %3d %3d %3d' % (a,E,k,nerr));
