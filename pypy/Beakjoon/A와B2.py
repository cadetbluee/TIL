import sys
sys.stdin=open('12919_input.txt')

S=input()
T=input()

def bfs(str):

    # print(str)
    if len(str)==len(S):
        return 1 if str==S else 0
    # elif n<len(S):
    #     return 0
    if str[-1]=='A':
        if bfs(str[:-1]):
            return 1
    if str[0]=='B':
        if bfs(str[1:][::-1]):
            return 1
    return 0
    # bfs(nstr[::-1],n+1)
print(bfs(T))
