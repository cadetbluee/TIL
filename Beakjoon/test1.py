N=int(input())
F=int(input())
A=N//100*100
while A%F!=0:
    A+=1
print(str(A)[-2:])