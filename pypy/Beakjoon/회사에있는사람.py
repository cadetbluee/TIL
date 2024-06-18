import sys
sys.stdin=open("7785_input.txt","r")
N=int(input())
name_list=set()
for i in range(N):
    name,log=input().split()
    if log=='enter':
        name_list.add(name)
    else:
        name_list.remove(name)
for i in sorted(name_list,reverse=True):
    print(i)