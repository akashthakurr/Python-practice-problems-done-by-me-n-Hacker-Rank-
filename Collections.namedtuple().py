N, C = int(input()), list(input().split())
print("%.2f" %float(sum((int(list(input().split())[C.index('MARKS')])) for _ in range(N)) / N))