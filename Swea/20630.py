def solution(n, edge):
    global count

    graph = [[] for _ in range(n + 1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    s = 1
    depth = [0] * (n + 1)
    stack = []
    for i in graph[1]:
        stack.append((1, i))
    while stack:
        d, a = stack.pop(0)
        depth[a] = d
        for i in graph[a]:
            stack.append((d + 1, i))
        if 0 not in depth:
            break

    print(depth)
    #     ans=[]

    #     for i in range(2,n+1):
    #         count=0
    #         recur(i,0,graph)
    #         ans.append(count)
    #     a=max(ans)
    #     answer=ans.count(a)

    return
solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])