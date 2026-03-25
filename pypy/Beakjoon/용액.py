import sys
sys.stdin=open('2467_input.txt')

N=int(input())
solutions=list(map(int,input().split()))

left=0
right=N-1

# 투포인터로 풀자
answer=100000
pair=[0,0]
while left<right:
    temp=solutions[left]+solutions[right]
  
    if answer>abs(temp):
        
        pair=[solutions[left],solutions[right]]
        answer=abs(temp)
    if temp>0 :
        right-=1
    elif temp<0 :
        left+=1
    else:
        break
    
print(*pair)

# for i in range(N):
#     for j in range(N):
#         if abs(solutions[i]+solutions[j])<answer:
#             pair=[solutions[i],solutions[j]]
#             answer=abs(solutions[i]+solutions[j])
# print(*pair)
