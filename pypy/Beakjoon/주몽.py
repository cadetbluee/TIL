import sys
sys.stdin=open('1940_input.txt')

N=int(input())
M=int(input())
ori=list(map(int,input().split()))
ori.sort()
right=0
left=N-1
count=0
while right<left:
    # print(ori,right,left)
    if ori[right]+ori[left]==M:
        count+=1
        right+=1
        left-=1
    elif ori[right]+ori[left]<M:
        right+=1
    elif ori[right]+ori[left]>M:
        left-=1
print(count)