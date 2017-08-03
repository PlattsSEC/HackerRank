// Created by C master Alex Lanzano


#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
	int number_of_socks;
	int number_of_pairs = 0;
	scanf("%d",&number_of_socks);
	int socks[101] = {0};
	for(int i = 0; i < number_of_socks; i++){
		int color;
		scanf("%d",&color);
		socks[color] += 1;
	}
	for(int color = 1; color < 101; color++){
		if(socks[color] == 0)
			continue;
		number_of_pairs += socks[color]/2;
	}
	printf("%d", number_of_pairs);
	return 0;
	
}
