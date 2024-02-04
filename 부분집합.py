arr=[3,4,5,6,7,1,2]

for i in range(1<<len(arr)):
    for j in range(len(arr)):
        if i &(1<<j):
            print(arr[j],end=' ')
    print()        