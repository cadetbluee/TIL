a,b,c,d,e,f=map(int,input().split())
if a==0:
    print(int((f-e*(c/b))/d)  ,int(c/b))
elif b==0:
    print(int(c/a),int((f-d*(c/a))/e))
elif d==0:
    print(int((c-b*(f/e))/a)  ,int(f/e))
elif e==0:
    print(int(f/d),int((c-a*(f/d))/b))
else:
    for y in range(-999,1000):
        if d*(((c)-(b)*y)/(a))+e*y==f:
            print(int(((c)-(b)*y)/(a)),y )
            break