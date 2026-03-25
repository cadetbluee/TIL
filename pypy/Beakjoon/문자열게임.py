import sys
sys.stdin=open('20437_input.txt')

T=int(input())
for _ in range(T):
    W=input()
    K=int(input())
    words=dict()
    for i in range(len(W)):
        word=W[i]
        if word in words:
            words[word].append(i)
        else:
            words[word]=[i]
    min_cnt=len(W)+1
    max_cnt=0
    for i,word in words.items():
        # print(word)
        if len(word)>=K:
            for j in range((K-1),len(word)):
                # print(word[j],word[j-(K-1)])
                min_cnt=min(word[j]-word[j-(K-1)]+1,min_cnt)
                max_cnt=max(word[j]-word[j-(K-1)]+1,max_cnt)
    if min_cnt==len(W)+1:
        print(-1)
    else:
        print(min_cnt,max_cnt)
    