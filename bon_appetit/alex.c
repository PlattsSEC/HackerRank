// Created by C master Alex Lanzano

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int items_ordered;
	int item_not_eaten;
	int amount_charged;
	int correct_amount_charged = 0;

	scanf("%d %d", &items_ordered, &item_not_eaten);
	
	for(int i = 0; i < items_ordered; ++i){
		int cost;
		scanf("%d", &cost);
		if(i != item_not_eaten)
			correct_amount_charged += cost;
	}
	correct_amount_charged /= 2;
	scanf("%d", &amount_charged);
	if(correct_amount_charged == amount_charged)
		printf("Bon Appetit");
	else{
		printf("%d", amount_charged-correct_amount_charged);
	}
	return 0;
	
}
