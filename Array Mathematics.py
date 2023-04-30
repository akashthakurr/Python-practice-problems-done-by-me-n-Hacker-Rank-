import numpy

n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for j in range(n):
    b.append(list(map(int,input().split())))

arr1 = numpy.array(a)
arr2 = numpy.array(b)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(arr1//arr2)
print(numpy.mod(a, b))
print(numpy.power(a, b))
