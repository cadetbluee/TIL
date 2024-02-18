import sys
sys.stdin=open("2149_input.txt")
key=input()
code=input()
len_str=len(code)//len(key)
coded_key=sorted(key)

arr=[[] for _ in range(len_str+1)]
arr[0].extend(coded_key)
for i in range(len_str):
    for j in range(len(key)):
        
        arr[i+1].append(code[j*len_str+i])
answer=[[] for _ in range(len_str)]

for k in key:
    for i, ch in enumerate(arr[0]):
        if k==ch:
            arr[0][i]=0
            for j in range(len_str):
                answer[j].append(arr[j+1][i])
            break
        
for i in answer:
    for j in i:
        print(j,end='')
