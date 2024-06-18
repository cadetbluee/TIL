def f(arr,N):
    for i in range(1,1<<N):#i가 공집합인경우 제외
        s=0
        for j in range(N):
            if i &(1<<j):
                s+=arr[j]
        if s==0:
            return True
