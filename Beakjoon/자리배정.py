def spiral_sequence(r,c,target):
    matrix = [[0]*c for _ in range(r)]
    
    top, bottom, left, right = 0, r-1, 0, c-1
    num = 1
    ans=[]
    while top <= bottom and left <= right:
        
        for i in range(left, right+1):
            matrix[top][i] = num
            if num==target:
                    ans.append((top,i))
            num += 1
        top += 1

        for i in range(top, bottom+1):
            matrix[i][right] = num
            if num==target:
                    ans.append((i,right))
            num += 1
        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                matrix[bottom][i] = num
                if num==target:
                    ans.append((bottom,i))
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                if num==target:
                    ans.append((i,left))
                num += 1
            left += 1


    return ans

C,R=map(int,input().split())
K=int(input())
if C*R<K:
    print(0)
else:
    arr=spiral_sequence(C,R,K)
    print(arr[0][0]+1,arr[0][1]+1)
    

