#!/bin/python
import sys

n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
# your code goes here

current_rank = 1
ranks = [1]*len(scores)
for i in range(1,len(scores)):
    if scores[i-1] != scores[i]:
        current_rank +=1
        ranks[i] = current_rank
    else:
        ranks[i] = current_rank

current_index = len(scores)-1
for j in alice:
    if j > scores[0]:
        print 1
    elif j < scores[-1]:
        print ranks[-1]+1
    else:
        while j > scores[current_index]:
            current_index -=1
        if j == scores[current_index]:
            print ranks[current_index]
        else:
            print ranks[current_index]+1