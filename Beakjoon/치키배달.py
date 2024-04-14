arr=input().split()
if arr[0]==arr[1]==arr[2]:
    result=int(arr[0])*1000+10000
elif arr[0]==arr[1] or arr[1]==arr[2]:
    result=int(arr[1])*100+1000
elif arr[2]==arr[0]:
    result=int(arr[0])*100+1000
else:
    result=int(max(arr))*100
    
print(result)