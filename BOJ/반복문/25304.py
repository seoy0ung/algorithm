x = int(input()) # 영수증에 적힌 총 금액
n = int(input()) # 영수증에 적힌 구매한 물건의 종류의 수
total = 0

for i in range(n):
    a, b = map(int, input().split())
    total += a * b

if total == x:
    print("Yes")
else:
    print("No")
