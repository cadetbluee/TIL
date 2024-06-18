def recur(l,r):
    global cnt
    cnt+=1
    if l>=r:
        return 1
    elif s[l]!=s[r]:
        return 0
    else:
        return recur(l+1,r-1)
    
t=int(input())
for _ in range(t):
    cnt=0
    s=input()
    print(recur(0,len(s)-1),cnt)