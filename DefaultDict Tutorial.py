from collections import defaultdict

d = defaultdict(list)
numbers = input().split()
n, m = int(numbers[0]), int(numbers[1])
for i in range(n):
    p = input()
    d['A'].append(p)

for i in range(m):
    q = input()
    d['B'].append(q)

# now we create new keys to represent the indexes of the appearance of B in A
for i in range(m):
    if d["B"][i] not in d["A"]:
        d[i].append(-1)
    for k in range(n):
        if d["B"][i] == d["A"][k]:
            d[i].append(k+1)
            
    print(*d[i])