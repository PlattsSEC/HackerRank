/*
 * Written by C master, Alex Lanzano
 */

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

#define GET_CHAR_VAL(x) x - 96

int main(){
    char* s = (char *)malloc(512000 * sizeof(char));
    int *weights = calloc(99512000, sizeof(int));
    scanf("%s",s);
    
    int weights_i = 0;
    int count = 0;
    char previous = 0;
    
    for(int i = 0; i < strlen(s); ++i){
        if (previous != s[i]){
            count = GET_CHAR_VAL((int)s[i]);
            weights[count] = 1;
            previous = s[i];
        } else {
            count += GET_CHAR_VAL((int)s[i]);
            weights[count] = 1;
        }
        
    }
    
    
    int n; 
    scanf("%d",&n);
    for(int a0 = 0; a0 < n; a0++){
        int x; 
        scanf("%d",&x);
        if (weights[x])
          printf("Yes\n");
        else
            printf("No\n");
    }
    return 0;
}
