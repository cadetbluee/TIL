# import random
# height=[]
# for i in range(9):
#     height.append(int(input()))
# sum_7=0
# while sum_7!=100:
#     rand_7=random.sample(height,7)
#     #print(rand_7)
#     sum_7=sum(rand_7)

# rand_7=sorted(rand_7)
# for i in range(7):
#     print(rand_7[i])
height=[]
for _ in range(9):
    height.append(int(input()))
sum_dwarf=sum(height)
for i in range(8):
    for j in range(i+1,9):
        if (sum_dwarf-height[i]-height[j])==100:
            height.pop(j)
            height.pop(i)
            break
    if len(height)==7:
        break
height.sort()
for i in height:
    print(i)