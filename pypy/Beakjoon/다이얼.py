word=input()
ans=0
for w in word:
    w=ord(w)-65
    if w>21:
        ans+=10
    elif w>18:
        ans+=9
    elif w>14:
        ans+=8
    else:
        ans+=w//3+3
print(ans)