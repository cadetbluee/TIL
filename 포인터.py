T=int(input())
for test in range(10):
    input_= input().split()
    size,txt = int(input_[0]), input_[1]
    stack = ['']*size
    top = -1

    for letter in txt:
        if top == -1 or letter != stack[top]:
            top+=1              # top 상단 이동
            stack[top] = letter # 최상단에 삽입

        elif letter == stack[top] :
            top-=1              # top 하단 이동
            stack[top+1] = ''   # 최상단 삭제

    print(f'#{test + 1} {"".join(stack)}')
#포인터를 사용하면 추가, 삭제하지 않아서 연산이 빠르다