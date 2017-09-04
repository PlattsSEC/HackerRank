// Made by C master Alex Lanzano

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int solve(int number_of_pages, int desired_page){
	int pages_turned = 0;
	if(desired_page == 1 || desired_page == number_of_pages)
		return 0;


	if(desired_page <= number_of_pages / 2){
		for(int page = 2; page <= number_of_pages; ++page){
			if(page % 2 == 0)
				++pages_turned;
			if(page == desired_page)
				break;
		}
	} else {

		for(int page = number_of_pages-1; page > 0; --page){
			
			if(page % 2 != 0)
				++pages_turned;
			if(page == desired_page)
				break;
		}
	}

	return pages_turned;
	
}

int main() {
	int n;
	scanf("%d", &n);
	int p;
	scanf("%d", &p);
	int result = solve(n, p);
	printf("%d\n", result);
	return 0;
	
}
