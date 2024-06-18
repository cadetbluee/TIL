import sys
sys.stdin=open("1269_input.txt")
A,B=map(int,input().split())
A_set=set(map(int,input().split()))
B_set=set(map(int,input().split()))
print(len(A_set-B_set)+len(B_set-A_set))