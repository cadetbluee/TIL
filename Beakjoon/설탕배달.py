N=int(input())
if N%5==0:
    print(N//5)
elif N%5==3:
    print(N//5+1)
elif N//5>=1 and N%5==1:
    print(N//5-1+2)
elif N//5>=1 and N%5==4:
    print(N//5-1+3)
elif N//5>=2 and N%5==2:
    print(N//5-2+4)
else:
    print(-1)