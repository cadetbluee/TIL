import sys
sys.stdin=open("1213_input.txt","")
for tc in range(10):
    test_case=input()
    str_find=input()
    txt=input()
    result=0
    for i in range(len(txt)-len(str_find)+1):
        cnt=0
        for j in range(len(str_find)):
            if txt[i+j]==str_find[j]:
                cnt+=1
        if cnt==len(str_find):
            result+=1
    print(result)