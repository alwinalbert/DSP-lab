#include <stdio.h>

void convolution(float* X,float* H,float* y,int M,int N){
    int n,k;
    int y_len = N+M-1;
    for (n = 0; n<y_len;n++){
        y[n] = 0;
        for(k=0;k<M;k++){
            if((n-k>=0)&&(n-k<N)){
                y[n] += X[k]*H[n-k];
            }
        }
        printf("%.2f ",y[n]);
    }
}

void main(){
    float X[] = {1.0f,2.0f,3.0f,4.0f};
    float H[] = {1.0f,1.0f,1.0f};
    int M = sizeof(X)/sizeof(float);
    int N = sizeof(H)/sizeof(float);
    float y[100];
    convolution(X,H,y,M,N);
}