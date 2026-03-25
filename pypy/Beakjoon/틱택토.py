import sys
sys.stdin=open('7682_input.txt')

winning_idx=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
while True:
    test_case=input()
    if test_case=='end':
        break
    x_count=test_case.count('X')
    o_count=test_case.count('O')
    if abs(o_count-x_count)>1 or x_count<o_count:
        print('invalid')
    else:
        X_win=0
        O_win=0
        for idx_list in winning_idx:
            O_cnt=0
            X_cnt=0
            for idx in idx_list:
                if test_case[idx]=='X':
                    X_cnt+=1
                elif test_case[idx]=='O':
                    O_cnt+=1
            if X_cnt==3:
                X_win+=1
            elif O_cnt==3:
                O_win+=1
        # 두번 이길때 올바른 경우는 마지막에 두는 수가 두번을 완성, 즉 X가 두번 이기는 경우 개수가 5개 4개여야 함 
        if X_win >1 or O_win>1:
            if (X_win>1 and x_count==5 and o_count==4) or (O_win>1 and o_count==5 and x_count==4):
                print('valid')
            else:
                print('invalid')
        # 한번씩 이겼을때는 무승부도 안되고 더 개수가 많은 쪽이 지는 것도 안됨.. 승부가 났는데 뒀다는거니깐
        elif X_win==1 or O_win==1:
            if X_win==1 and O_win==1:
                print(3,'invalid')
            elif (X_win==1 and x_count<=o_count) or (O_win==1 and x_count>o_count):
                print(4,'invalid')
            else:
                print(5,'valid')
        else:
            if x_count+o_count==9:
                print(6,'valid')
            else:
                print(7,'invalid') 