import sys
sys.stdin = open("4843_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    result=[]
    list_n=list(map(int,input().split()))
    for _ in range(N//2):
        for i in range(N-1):
            minIdx=i
            for j in range(i+1,N):
                if list_n[minIdx]>list_n[j]:
                    minIdx=j
            list_n[i],list_n[minIdx]=list_n[minIdx],list_n[i]
        result.append(list_n.pop(len(list_n)-1))
        result.append(list_n.pop(0))
        N=len(list_n)
    if len(list_n)==1:
        result.append(list_n(0))
    print(f'#{test_case}',*result[:10])