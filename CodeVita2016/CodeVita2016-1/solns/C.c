#include <stdio.h>

int main(){
    long i, j, N, p;
    scanf("%ld", &N);
    long A[N+1]; 
    for(i=0; i<=N; i++) A[i]=i;

    for(p=2; p*p<=N; p++){
        if(A[p] !=0)for(i=p*2; i<=N; i+=p)A[i]=0;
        
    }
    //A[1]=0;
    //for(i=0; i<=N; i++) printf("%ld\n", A[i]);
    //So Far So good
    long sum = 5, count =0;
    for(j=5; j<=N; j=j+2){
        //printf("j: %ld\n", j);
        if( (A[j] !=0 && A[j] == sum) || A[j] == -1) count = count + 1;
        if(A[j] != 0 || A[j] == -1){
            sum = sum + j;
            if( A[sum] != 0)A[sum] = -1;
        }
            //printf("count: %ld\n", count);
    }

    //output
    printf("count: %ld\n", count);
}