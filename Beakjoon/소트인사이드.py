A=input()
arr=[]
for a in A:
    arr.append(a)
arr.sort(reverse=True)
for a in arr:
    print(a,end='')