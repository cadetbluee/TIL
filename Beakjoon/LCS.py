A=input()
B=input()
result=0
for a in range(len(A)):
    if A[a] in B:
        string=''
        for i in range(a,len(A)):
            string+=A[i]
            if string not in B:
                result=max(result,len(string))
                break
print(result)