import sys
sys.stdin=open("1225_input.txt")
T=10
# Q=[0]*10
# front = -1  # 마지막으로 꺼낸 위치
# rear = -1  # 마지막저장위치
# def enQueue(A):
#     global rear
#     rear+=1
#     Q[rear]=A
# def deQueue():
#     global front
#     front+=1
#     return Q.pop(front)
# def isEmpty():
#     return front==rear
# def isFull():
#     return rear==len(Q)-1
# def Qpeek():
#     if isEmpty():print("Queue_Empty")
#     else: return Q[front+1]
for tc in range(1,T+1):
    n=int(input())
    n_list=list(map(int,input().split()))
    # Q = [0] * 8
    # for q in range(8):
    #     Q[q]=n_list[q]
    # print(Q)
    i=1
    while n_list[7]>0:
        a=n_list.pop(0)
        n_list.append(a-i)
        if i==5:
            i=1
        else:
            i+=1
    if n_list[7]<0:
        n_list[7]=0
    print(f'#{tc}',*n_list)