# def recur(i,j):
#     if i==j:
#         print(*arr)
#         return
#     l=i+(j-i)//3
#     r=i+((j-i)//3)*2
#     for k in range(l,r):
#         arr[k]=' '
#     recur(i,l)
#     recur(r,j)
# n=int(input())
# arr=['-']*(3**n)

# recur(0,3**n)
def solve(n):
    if n == 1:
        return "-"
    else:
        left = solve(n // 3)
        center = " " * (n // 3)
        return left + center + left

while True:
    try:
        N = int(input())

        rst = solve(3 ** N)
        print(rst)
    except:
        break

