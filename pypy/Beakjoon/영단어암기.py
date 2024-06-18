# import sys
# sys.stdin=open("20920_input.txt")
# N,M=map(int,input().split())
# voca={}
# voca_list=[]
# for _ in range(N):
#     s=input()
#     if len(s)>=M:
#         if s not in voca:
#             voca_list.append(s)
#             voca[s]=1
#         else:
#             voca[s]+=1
# pre_v=0
# pre_idx=0
# pre_k=''
# i=0
# while i!=len(voca_list)-1:
#     if voca[voca_list[i]]<voca[voca_list[i+1]]:
#         voca_list[i],voca_list[i+1]=voca_list[i+1],voca_list[i]
#         i=0
#     elif voca[voca_list[i]]==voca[voca_list[i+1]]:
#         if len(voca_list[i])<len(voca_list[i+1]):
#             voca_list[i],voca_list[i+1]=voca_list[i+1],voca_list[i]
#             i=0
#         elif len(voca_list[i])==len(voca_list[i+1]):
#             if voca_list[i]>voca_list[i+1]:
#                 voca_list[i],voca_list[i+1]=voca_list[i+1],voca_list[i]
#                 i=0
#             else:
#                 i+=1
#         else:
#             i+=1
#     else:
#         i+=1
# for i in voca_list:
#     print(i)
import sys
from collections import defaultdict

# 입력 리디렉션 설정
sys.stdin = open("20920_input.txt")

# 입력 받기
N, M = map(int,sys.stdin.readline().split())
voca = defaultdict(int)

# 단어 카운트
for _ in range(N):
    s = sys.stdin.readline().strip()
    if len(s) >= M:
        voca[s] += 1

# 정렬 기준: 빈도수가 높은 것이 우선, 그 다음에는 길이가 긴 단어가 우선, 길이가 같을 경우 알파벳 순서로 정렬
sorted_voca = sorted(voca.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 출력
for word, count in sorted_voca:
    print(word)
