import random
height=[]
for i in range(9):
    height.append(int(input()))
sum_7=0
while sum_7!=100:
    rand_7=random.sample(height,7)
    #print(rand_7)
    sum_7=sum(rand_7)

rand_7=sorted(rand_7)
for i in range(7):
    print(rand_7[i])