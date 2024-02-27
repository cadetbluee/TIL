import sys
sys.stdin=open('1247_input.txt')


def min_length(i,N,s):
    global min_sum
    if i==N:
        if s+abs(cos[idx[i]][0]-cos[idx[i-1]][0])+abs(cos[idx[i]][1]-cos[idx[i-1]][1])<min_sum:
            min_sum=s+abs(cos[idx[i]][0]-cos[idx[i-1]][0])+abs(cos[idx[i]][1]-cos[idx[i-1]][1])
        return
    elif s>min_sum:
        return
    for j in range(1,N):
        if j not in idx[:i]:
            idx[i]=j
            min_length(i+1,N,s+abs(cos[idx[i]][0]-cos[idx[i-1]][0])+abs(cos[idx[i]][1]-cos[idx[i-1]][1]))


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    office=(arr[0],arr[1])
    home=(arr[2],arr[3])
    cos=[office]
    for i in range(4,4+2*N,2):
        cos.append((arr[i],arr[i+1]))
    cos.append(home)
    idx=[0]*len(cos)
    idx[-1]=len(cos)-1
    min_sum=1e9
    min_length(1,len(cos)-1,0)
    print(f'#{tc} {min_sum}')