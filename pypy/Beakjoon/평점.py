import sys
sys.stdin=open('./25206_input.txt')
total=0
hak=0
grades={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
for _ in range(20):
    subject,score,grade=input().split()
    if grade !='P':
        total+=float(score)*grades[grade]
        hak+=float(score)
print(total/hak)