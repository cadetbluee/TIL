arr=[-1,3,-9,6,7,-6,1,5,4,-2]

for i in range(1<<10):
    sub=[]
    sum_sub=0
    for j in range(10):
        if i & (1<<j):
            sum_sub+=arr[j]
            sub.append(arr[j])
    if sum_sub==0:
        print(sub)


person=[15,30,50,10]
n=len(person)
person.sort()
sum=0
left_person=n-1
for turn in range(n):
    time=person[turn]
    sum+=left_person*time
    left_person-=1
print(sum)

n=3
target=30
things=[(5,50),(10,60),(20,140)]
things.sort(key=lambda x:(x[1]/x[0]),reverse=True)
sum=0
for kg,price in things:
    per_price=price/kg
    if target<kg:
        sum+=target*per_price
        break
    sum+=price
    target-=kg
print(int(sum))

