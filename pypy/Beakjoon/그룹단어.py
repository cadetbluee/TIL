N=int(input())
cnt=0
for _ in range(N):
    word=input()
    lst=[]
    pre=''
    isGroup=True
    for w in word:
        if w not in lst:
            lst.append(w)
        elif pre==w:
            continue
        else:
            isGroup=False
            break
        pre=w
    if isGroup:
        cnt+=1
print(cnt)