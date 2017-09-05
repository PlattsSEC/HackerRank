/* 
 * Created by Alex Lanzano
 */


#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>


struct date
{
	int day;
	int month;
	int year;
};

void get_date_difference(struct date *date_difference,
						 struct date *date_returned,
						 struct date *date_expected)
{
	date_difference->day = date_returned->day - date_expected->day;
	date_difference->month = date_returned->month - date_expected->month;
	date_difference->year = date_returned->year - date_expected->year;
	//printf("%d\n%d\n%d\n", date_difference->day, date_difference->month, date_difference->year);
}

uint32_t get_fine(struct date *difference)
{	
	if (difference->year > 0) {
		return 10000;
	} else if (difference->year < 0) {
		return 0;
	} else if (difference->month > 0) {
		return 500 * difference->month;
	} else if (difference->month < 0) {
		return 0;
	} else if (difference->day > 0) {
		return 15 * difference->day;
	} else {
		return 0;
	}
}

int main()
{
	struct date date_returned;
	struct date date_expected;
	struct date date_difference;
	uint32_t fine;
	
	scanf("%d %d %d", &date_returned.day, &date_returned.month, &date_returned.year);
	scanf("%d %d %d", &date_expected.day, &date_expected.month, &date_expected.year);
	get_date_difference(&date_difference, &date_returned, &date_expected);
	printf("%u\n", get_fine(&date_difference));
}
