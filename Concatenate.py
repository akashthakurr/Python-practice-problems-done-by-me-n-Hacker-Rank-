import numpy
n,m,p=map(int,input().split())

a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
b=[]
for i in range(m):
    b.append(list(map(int,input().split())))
    
    
print(numpy.concatenate((numpy.array(a),numpy.array(b)),axis=0))