import sys
sys.stdin=open("4871_input.txt")


def dfs(i,V,G):
    visited=[0]*(V+1)
    st=[]
    visited[i]=1
    while True:
        for w in adjl[i]:
            if visited[w]==0:
                st.append(i)
                i=w
                visited[i]=1
                if i==G:
                    return 1
                break
        else:
            if st:
                i=st.pop()
            else:
                break
    return 0


T = int(input())
for test_case in range(1, T + 1):
    V,E=map(int, input().split())
    adjl = [[] for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
    S,G=map(int, input().split())
    print(f'#{test_case}', end=' ')
    print(dfs(S, V,G))