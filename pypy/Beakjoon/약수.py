N=int(input())
if N%2==0:
    lst=list(map(int,input().split()))
    lst=sorted(lst)
    print(lst[0]*lst[-1])
else:
    lst=list(map(int,input().split()))
    lst=sorted(lst)
    print(lst[len(lst)//2]**2)