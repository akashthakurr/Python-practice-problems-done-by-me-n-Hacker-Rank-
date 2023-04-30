from collections import Counter
_, inventory, N, sales = input(), Counter(map(int, input().split())), int(input()), 0
for _ in range(N):
    size, price = (map(int, input().split()))
    remaining = inventory[size]
    if remaining > 0:
        inventory[size] -= 1
        sales += price
print(sales)