import sys
sys.stdin=open("19785_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    str_1=input().strip('\"')
    cnt_list=[]
    stand=0
    for n in range(1,len(str_1)):
        cnt=0
        for i in range(len(str_1)):
            if str_1[i:i+n]==str_1[i+n:i+n*2]:
                cnt+=1
        if cnt>=1:
            cnt_list.append(n)
            stand=n

    min_result=len(str_1)
    for stand in cnt_list:
        str_2 = str_1
        result = set()
        i = 0
        cnt=0
        while i<len(str_2):
            if str_2[i:i+stand]==str_2[i+stand:i+stand*2]:
                result.add(str_2[i:i+stand])
                str_2=str_2[:i]+str_2[i+stand:]
                i=0
                cnt+=1
            else:
                if i==0 and cnt==0:
                    break
                i+=1
        if min_result>(len(str_2)+len(result)):

            min_result=len(str_2)+len(result)

    print(f'#{test_case} {min_result}')