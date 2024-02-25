N=int(input())
numbers=[]
for _ in range(N):
    num=int(input())
    numbers.append(num)
sum_num=sum(numbers)
numbers=sorted(numbers)
num_counts = {w:numbers.count(w) for w in set(numbers)}
print(sum_num/N)