#include <stdio.h>
void convolve(float* x,float* h,float* y,int M, int N){
    int L = N+M-1;
    int n,k;
    for (n=0;n<L;n++){
        y[n] =0;
        for (k=0;k<N;k++){
            if(n-k>=0 && n-k<M){
                y[n] +=x[k]*h[n-k];
            }
        }
        printf("%.2f ",y[n]);
    }
}

void main(){
    float x[] = {1,-2,0,0,3};
    float h[] = {1};
    float y[100];
    int N = sizeof(x)/sizeof(float);
    int M = sizeof(h)/sizeof(float);
    convolve(x,h,y,M,N);
}