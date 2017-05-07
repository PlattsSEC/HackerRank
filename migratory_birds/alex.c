// Made by C master Alex Lanzano


#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stddef.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
	int n;
	int most_common_type = 0;
	int most_common_amount = 0;
	scanf("%d",&n);
	int *birds = calloc(n+1, sizeof(int));
	for(int i = 0; i < n; i++){
		int type;
		scanf("%d", &type);
		birds[type] += 1;
		if(birds[type] > most_common_amount){
			most_common_amount = birds[type];
			most_common_type = type;
		}
		if(birds[type] == most_common_amount &&
		   type < most_common_type){
			most_common_type = type;
		}
		    
	}
	printf("%d", most_common_type);
	return 0;
	
}
