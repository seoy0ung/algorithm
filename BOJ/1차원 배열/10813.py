n, m = map(int, input().split())
basket = [0] * n

for i in range(n):
    basket[i] = i + 1


for _ in range(m):
    i, j = map(int, input().split())
    n,m = basket[i-1], basket[j-1]
    basket[i-1] = m
    basket[j-1] = n


print(*basket)
