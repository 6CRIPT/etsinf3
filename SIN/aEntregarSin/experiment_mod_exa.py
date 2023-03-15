import sys 
import math
import numpy as np
from perceptron import perceptron
from confus import confus
from linmach import linmach

if len(sys.argv) != 4:
    print('Usage: %s <data> <alphas> <bs>' % sys.argv[0])
    sys.exit(1)


data = np.loadtxt(sys.argv[1])
alphas = np.fromstring(sys.argv[2], sep=' ')
bs = np.fromstring(sys.argv[3], sep=' ')

#
#organizar datos
N,L=data.shape; 
D=L-1;
labs=np.unique(data[:,L-1]); 
C=labs.size;
#dividir entrenamiento y test
np.random.seed(23); 
perm=np.random.permutation(N);
data=data[perm];

NTr=int(round(.8*N));
train=data[:NTr,:];

M=N-NTr;
test=data[NTr:,:]; #los datos que usaremos en el test iran desde la fila Ntr en adelante, y usamos toda la columna

print('#     a          b       E       k       Ete    Ete (%) Ite(%)');
print('#-------     -------    ----    ----    -----   ------- ----------');
#
for a in alphas:
    for b in bs:
         w,E,k=perceptron(train,b,a, K=150); 
         rl=np.zeros((M,1));
         for m in range(M):
             tem=np.concatenate(([1],test[m,:D]));
             rl[m]=labs[linmach(w,tem)];
         nerr,m=confus(test[:,L-1].reshape(M,1),rl);
         per = nerr/M;
         nerrPorcentaje = 1.96*math.sqrt(per*(1-per)/M);
         I = (per-nerrPorcentaje, per + nerrPorcentaje);
         print('%8.1f \t%3.1f\t%3d\t%3d\t%3d\t%3.1f\t[%3.1f, %3.1f]' % (a,b, E,k,nerr,per*100,(per-nerrPorcentaje)*100, (per+nerrPorcentaje)*100))
               

   