import sys
sys.stdin=open('5189_input.txt')

def min_elec(i,N,s):
    global min_e
    if i==N:
        if s+arr[idx[i-1]-1][idx[i]-1]<min_e:
            min_e=s+arr[idx[i-1]-1][idx[i]-1]
        return
    for j in range(2,N+1):
        if j not in idx[:i]:
            idx[i]=j
            min_elec(i+1,N,s+arr[idx[i-1]-1][idx[i]-1])

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx=[0]*N
    idx[0]=1
    idx.append(1)
    min_e=1e9
    min_elec(1,N,0)
    print(f'#{tc} {min_e}')