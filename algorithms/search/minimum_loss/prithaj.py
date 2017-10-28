import sys

n = input()
prices = map(int, raw_input().split())
price_map = {prices[i]:i for i in range(n)}
prices.sort()
min_loss = sys.maxint

for j in range(n-1):
    elem, elem2 = prices[j], prices[j+1]
    if price_map[elem] > price_map[elem2]:
        min_loss = min(min_loss,abs(elem2-elem))
print min_loss