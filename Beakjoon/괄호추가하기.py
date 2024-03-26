import sys
input = sys.stdin.readline
N = int(input())
num_str = input().strip()
visit = [0] * (N + 1)    
li = []
max_num = -2**31
if N == 1:
    max_num = int(num_str[0])
 
 
def result(arr):
    number = int(arr[0])
 
    for i in range(1, len(arr) - 1, 2):
        if arr[i] == '+':
            number += int(arr[i + 1])
        elif arr[i] == '-':
            number -= int(arr[i + 1])
        else:
            number *= int(arr[i + 1])
 
    return number

 
 
def calculate(x):
    global max_num
    if len(li) > 0:
 
        arr = []
        i = 0
    
        while i < len(num_str):
    
            if i in li:
                a = arr.pop()
                if num_str[i] == '+':
                    num = int(a) + int(num_str[i + 1])
                    arr.append(str(num))
                    i += 2
                elif num_str[i] == '*':
                    num = int(a) * int(num_str[i + 1])
                    arr.append(str(num))
                    i += 2
                elif num_str[i] == '-':
                    num = int(a) - int(num_str[i + 1])
                    arr.append(str(num))
                    i += 2
            else:
                arr.append(num_str[i])
                i += 1
        r=result(arr)
        if max_num < r:
            max_num = r
 
    if x == N:
        return

    for i in range(x, N, 2):
 
        if visit[i] == 1:
            continue
        visit[i] = visit[i + 2] = 1
        li.append(i)
        calculate(i + 4)
        li.pop()
        visit[i] = visit[i + 2] = 0
 
 
calculate(1)
print(max_num)