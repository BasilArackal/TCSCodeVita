#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, k, temp, diff, product;
    scanf("%d %d", &n, &k);
    int A[n], B[n];
    for(int i=0; i<n; i++){
        scanf("%d", &A[i]);    
    }
    for(int i=0; i<n; i++){
        scanf("%d", &B[i]);    
    }
    
    int maxDiff =0, minimumSum =0;
    for(int i=1; i<=n; i++){
        product = A[i] * B[i];
        if(product<0 && B[i] < 0) 
            temp = (A[i] + 2*k) * B[i];

        else if(product<0 && A[i] < 0)
            temp = (A[i] - 2 * k) * B[i];

        else if( product > 0 && A[i] < 0)
            temp = (A[i] + 2 * k) * B[i];

        else if (product > 0 && A[i] > 0)
               temp = (A[i] - 2 * k)  * B[i];
           
        diff =  abs(product - temp);
        if(diff > maxDiff) maxDiff = diff;
        minimumSum = minimumSum + product;
    }
    minimumSum = minimumSum - maxDiff;

    printf("%d\n", minimumSum);

}