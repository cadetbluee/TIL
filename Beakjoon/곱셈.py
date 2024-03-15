A,B,C=map(int,input().split())
if A==1:
    print(A%C)
elif A<C:
    rests=[A%C]
    while A<C:
        A*=A
        rests.append(A%C)
    end=len(rests)
    rest=0
    while rest!=rests[end-1]:
        A*=A
        rest=A%C
        rests.append(rest)
        print(rests)
    if B<len(rests):
        print(rests[B-1])
    elif B%(len(rests)-end)==0:
        print(rests[-2])
    else:
        print(rests[(end-2)+B%(len(rests)-end)])
else:
    rests=[A%C]
    rest=0
    end=0
    while rest!=rests[0]:
        A*=A
        rest=A%C
        rests.append(rest)
        print(rests)
    if B<len(rests):
        print(rests[B-1])
    elif B%(len(rests)-end)==0:
        print(rests[-2])
    else:
        print(rests[(end-2)+B%(len(rests)-end)])