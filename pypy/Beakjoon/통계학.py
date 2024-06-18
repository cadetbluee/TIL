from collections import Counter
import sys
N = int(sys.stdin.readline().strip())
numbers={}
num_list=[]
for _ in range(N):
    num=int(sys.stdin.readline().strip())
    if num not in numbers:
        numbers[num]=1
    else:
        numbers[num]+=1
    num_list.append(num)
sum_num=0
num_list=sorted(num_list)

max_count=max(numbers.values())
max_values=[]
for k,v in numbers.items():
    sum_num+=int(k)*v
    if v==max_count:
        max_values.append(int(k))
max_values=sorted(max_values)
print(round(sum_num/N))
print(num_list[N//2])
if len(max_values)>1: print(max_values[1]) 
else: print(max_values[0])
print(num_list[-1]-num_list[0])