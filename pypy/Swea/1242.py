import sys
sys.stdin = open("1242_input.txt", "r")
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=list(set(input().strip() for _ in range(N)))
    code=['211','221','122','411','132','231','114','312','213','112']
    b_code = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
            '1101', '1110', '1111']
    x_code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    N = len(arr)
    result=0
    for i in range(N):
        temp=''
        for j in range(M):
            temp+=b_code[x_code.index(arr[i][j])]
        arr[i]=temp
    M=len(arr[0])
    cnt0=0
    cnt1=0
    for i in range(N):
        temp=[]
        for j in range(M):
            if arr[i][j]=='0':
                if cnt1>0:
                    temp.append(cnt1)
                    cnt1=0
                cnt0+=1
            else:
                if cnt0>0:
                    temp.append(cnt0)
                    cnt0=0
                cnt1+=1
        if cnt1>0:temp.append(cnt1)
        arr[i]=temp
    re=set()
    
    while len(arr)>0:
        temp=arr.pop()
        if temp not in arr:
            ans=[]
            for j in range(0,len(temp),4):
                x=min(temp[j+1],temp[j+2],temp[j+3])
                # if tc==1:print(str(int(temp[j+1]/x))+str(int(temp[j+2]/x))+str(int(temp[j+3]/x)))
                if str(int(temp[j+1]/x))+str(int(temp[j+2]/x))+str(int(temp[j+3]/x)) in code:
                    num=code.index(str(int(temp[j+1]/x))+str(int(temp[j+2]/x))+str(int(temp[j+3]/x)))
                    ans.append(num)
                    # if tc==1:print(num)
            
            for i in range(0, len(ans), 8) : #8개씩 잘라서 넣기
                re.add(tuple(ans[i:i+8]))
    # if tc==1:print(re)
    for temp in re:
        even, odd = 0, 0
        for k in range(8):
            if k % 2 == 0:
                odd += temp[k]
            else:
                even += temp[k]
        if (odd * 3 + even) % 10 == 0:
            result += odd + even
     
    print(f'#{tc}',result)
    # codes=set()
    # arr=list(arr)
    # N=len(arr)
    # for b in range((M//14)*14,13,-14):
    #     for i in range(N):
    #         j = M - 1
    #         while j>=0:
    #             if arr[i][j]!='0'and (j-b-1)>0:
    #                 c=arr[i][j-b:j+1].strip('0')
    #                 if len(c)>=b:codes.add(c)
    #                 j=j-b-1
    #             else:
    #                 j-=1
    # if tc==9 :
    #     print(codes)
    # result=0
    # for i in codes:
    #     even = 0
    #     odd = 0
    #     a = len(i) // 14
    #     i='0'*a+i
    #     ans=''
    #     for j in i:
    #         ans+=b_code[x_code.index(j)]
    #     for l in range(len(ans)-1,-1,-1):
    #         if ans[l]=='1':
    #             ans=ans[l-56*a+1:l+1]
    #             break
    #     a = len(ans) // 56
    #     for k in range(1,9):
    #         if k%2==0:
    #             s=ans[(k-1)*a*7:k*a*7]
    #             cnt0=0
    #             cnt1=0
    #             m=0
    #             ran=[]
    #             while m<len(s):
    #                 if s[m]=='0':
    #                     if cnt1>0:ran.append(cnt1)
    #                     cnt1=0
    #                     cnt0+=1
    #                 else:
    #                     if cnt0>0:ran.append(cnt0)
    #                     cnt0=0
    #                     cnt1+=1
    #                 m+=1
    #             ran.append(cnt1)
    #             if len(ran) == 4:
    #                 ran=[int(x/a) for x in ran]
    #                 if ran in code:
    #                     even+=code.index(ran)
    #                 else:
    #                     break
    #             else:
    #                 break
    #         else:
    #             s=ans[(k - 1) * a * 7:k * a * 7]
    #             cnt0=0
    #             cnt1=0
    #             m=0
    #             ran=[]
    #             while m<len(s):
    #                 if s[m]=='0':
    #                     if cnt1>0:ran.append(cnt1)
    #                     cnt1=0
    #                     cnt0+=1
    #                 else:
    #                     if cnt0>0:ran.append(cnt0)
    #                     cnt0=0
    #                     cnt1+=1
    #                 m+=1
    #             ran.append(cnt1)
    #             if len(ran)==4:
    #                 ran=[int(x/a) for x in ran]
    #                 if ran in code:
    #                     odd += code.index(ran)
    #                 else:
    #                     break
    #             else:
    #                 break
    #
    #     if (odd*3+even)%10==0:
    #         result+=(odd+even)
   