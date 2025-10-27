#include <stdio.h>
#include <math.h>
#define PI 3.14

typedef struct{
    float real;
    float imag;
} Complex;

void dft(float* x, Complex* X, int N){
    int n,k;
    for(k=0;k<N;k++){
        X[k].real = 0;
        X[k].imag = 0;
        for(n=0;n<N;n++){
            X[k].real += x[n]*cos(-2*PI*k*n/N);
            X[k].imag -= x[n]*sin(-2*PI*k*n/N);
        }
        printf("\n%.2f",X[k].real,X[k].imag);
    }

}

void main(){
    float x[32];
    int N = sizeof(x)/sizeof(float);
    int i;
    for (i=0;i<N;i++){
        x[i] = sin(2*PI*2000*i/8000);
    }
    Complex X[100];
    dft(x,X,N);
}