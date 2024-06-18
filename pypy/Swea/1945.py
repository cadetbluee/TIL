import sys
sys.stdin = open("1945_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    number=int(input())
    num_list=[]
    div_list=[11,7,5,3,2]
    for i in div_list:
        while number%i==0:
            num_list.append(i)
            number=int(number/i)
    result=[]
    for i in range(5):
        cnt=0
        for j in range(len(num_list)):
            if div_list[i]==num_list[j]:
                cnt+=1
        result.append(cnt)
    print(f'#{test_case}',end=' ')
    result=result[::-1]
    for i in range(5):
        if i!=4:
            print(result[i],end=' ')
        else:
            print(result[i])