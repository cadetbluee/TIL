n=int(input())
i=0
max_i=0
while i**2<=n:
    if max_i<i**2:
        max_i=i**2
    i+=1
print(i-1)