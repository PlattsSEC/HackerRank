/*
 * This was made by Alex Lanzano
 */


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>



int ascending_order(const void *a, const void *b)
{
	return *(const uint32_t *)a - *(const uint32_t *)b;
}

int descending_order(const void *a, const void *b)
{
	return *(const uint32_t *)a + *(const uint32_t *)b;
}


int32_t get_money_spent(uint32_t *cont1, uint32_t cont1_size,
						uint32_t *cont2, uint32_t cont2_size,
						uint32_t money)
{
	int ret = -1;
	int money_spent;
	for (int i = 0; i < cont2_size; ++i) {
		money_spent = cont1[i] + cont2[i];
		if (money_spent > money)
			money_spent = -1;
		if (money_spent > ret)
			ret = money_spent;
	}
	
	return ret;
}

int main()
{
	uint32_t money;
	int32_t money_spent;
	uint32_t keyboards_size;
	uint32_t drives_size;

	/* NEVER ACTUALLY USE SCANF!!!
	 * IT'S REALLY UNSAFE!!!
	 */
	scanf("%d %d %d", &money, &keyboards_size, &drives_size);

	uint32_t keyboards[keyboards_size];
	uint32_t drives[drives_size];

	/* This just grabs the prices for each keyboard and drives */
	for (int keyboards_i = 0; keyboards_i < keyboards_size; ++keyboards_size) {
		scanf("%d", &keyboards[keyboards_i]);
	}
	
	qsort(keyboards, keyboards_size, sizeof(uint32_t), ascending_order);
	
	for (int drives_i = 0; drives_i < drives_size; ++drives_i) {
		scanf("%d", &drives[drives_i]);
	}
	printf("hello\n");

	qsort(drives, drives_size, sizeof(uint32_t), descending_order);

	if (keyboards_size > drives_size)
	    money_spent = get_money_spent(keyboards, keyboards_size, drives, drives_size, money);
	else
	    money_spent = get_money_spent(drives, drives_size, keyboards, keyboards_size, money);
		
	
	
	printf("%d\n", money_spent);
	return 0;
}
