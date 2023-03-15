#include <stdio.h>
#include <stdlib.h>
void main(){
#pragma omp parallel
 {
  #pragma omp for
  for(int n=0; n<10; ++n)
    printf(" %d", n);
    printf (omp_get_thread_num());
    

 }
}
 