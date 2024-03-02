import sys
sys.stdin=open('4366_input.txt')
T=int(input())
for tc in range(1,T+1):
    bi_num=list(input().strip())
    tri_num=list(input().strip())
    ans=0
    for i in range(len(bi_num)):
        for j in range(len(tri_num)):
            if tri_num[j]=='2':
                bi_num[i] =str(1- int(bi_num[i]))
                tri_num[j]='1'
                if int(''.join(bi_num),2)==int(''.join(tri_num),3):
                    ans=int(''.join(bi_num),2)
                tri_num[j]='0'
                if int(''.join(bi_num), 2) == int(''.join(tri_num), 3):
                    ans = int(''.join(bi_num), 2)
                bi_num[i] = str(1 - int(bi_num[i]))
                tri_num[j] = '2'
            elif tri_num[j]=='1':
                bi_num[i] = str(1 - int(bi_num[i]))
                tri_num[j] = '2'
                if int(''.join(bi_num), 2) == int(''.join(tri_num), 3):
                    ans = int(''.join(bi_num), 2)
                tri_num[j] = '0'
                if int(''.join(bi_num), 2) == int(''.join(tri_num), 3):
                    ans = int(''.join(bi_num), 2)
                bi_num[i] = str(1 - int(bi_num[i]))
                tri_num[j] = '1'
            else:
                bi_num[i] = str(1 - int(bi_num[i]))
                tri_num[j] = '2'
                if int(''.join(bi_num), 2) == int(''.join(tri_num), 3):
                    ans = int(''.join(bi_num), 2)
                tri_num[j] = '1'
                if int(''.join(bi_num), 2) == int(''.join(tri_num), 3):
                    ans = int(''.join(bi_num), 2)
                bi_num[i] = str(1 - int(bi_num[i]))
                tri_num[j] = '0'
            if ans:
                break
        if ans:
            break
    print(f'#{tc} {ans}')