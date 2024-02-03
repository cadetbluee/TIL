# %%
# 리스트 컴프리헨션 연습
# (1) 짝수만 있는 리스트 만들기
nums = [1,2,3,4,5,6,7]
even_nums = []
for n in nums :
    if n % 2 == 0 :
        even_nums.append(n)
even_nums=[n for n in nums if n%2==0]
print(even_nums)
#%%
# (2) 리스트에서 음수제거 하기
nums = [-1,2,-3,-4,-5,-6,7]
posi_nums=[n for n in nums if n>0]
print(posi_nums)

# (3) 다음 숫자 리스트의 요소를 제곱한 리스트를 만들기
nums = [1,2,3,4,5,6,7]
pow_nums=[n**2 for n in nums]
print(pow_nums)
# (4) 문자열 리스트에서 길이가 5이상인 단어만 선택
words = ['apple', 'banana', 'cherry', 'bam', 'bae']
above_5=[w for w in words if len(w)>5]
print(above_5)
# (5) 문자열 리스트에서 문자열의 공백이 포함된 경우 공백을 제거한 리스트 만들기
words = [' apple  ', ' banana ', ' cherry ', 'bam', 'bae     ']
no_space=[w.strip() for w in words]
print(no_space)
# (6) 다음 학생들의 짝궁을 결정 짓기 위해 모든 짝궁의 조합을 구하시오
names = ['해인', '고은', '두홍', '봉준', '온겸']
# 아래가 출력될 수 있도록 함
# [('해인', '고은'), ('해인', '두홍'), ('해인', '봉준'), ('해인', '온겸'), ('고은', '해인'), ('고은', '두홍'), ('고은', '봉준'), ('고은', '온겸'), ('두홍', '해인'), ('두홍', '고은'), ('두홍', '봉준'), ('두홍', '온겸'), ('봉준', '해인'), ('봉준', '고은'), ('봉준', '두홍'), ('봉준', '온겸'), ('온겸', '해인'), ('온겸', '고은'), ('온겸', '두홍'), ('온겸', '봉준')]print([(n1,n2) for n1 in names for n2 in names if n1!=n2 ])
two_pair=[(a,b) for a in names for b in names  if a!=b ]
print(two_pair)
# (7) 2차원 리스트의 모든 요소를 제곱하여 새로운 2차원 리스트 생성
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in matrix:
#     for j in i:
#         j**2
pow_matrix=[[a**2 for a in i] for i in matrix]
print(pow_matrix)
# 아래가 출력될 수 있도록 함
#[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
#%%
# 리스트 컴프리헨션 이중 for문
# (1) 구구단 만들기
gugu = []
for i in range(1,10) :
    for j in range(1,10) :
        gugu.append(f'{i}x{j}={i*j}')
print(gugu)

gugu = [f'{i}x{j}={i*j}' for i in range(1,10) for j in range(1,10)]
print(gugu)

# (2) 2차원 리스트를 1차원 리스트로 변환하기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [i for j in matrix for i in j]
print(flatten)

# (3) 리스트의 조합 생성
colors = ['red', 'green', 'blue']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)

# %%
# 딕셔너리 컴프리헨션 
#(1) 두 리스트를 키와 값으로 하는 딕셔너리 만들기
subjects = ['math', 'history', 'english', 'computer science']
grades = ['A', 'B', 'C', 'A']
grade_dict = {subject:grade for subject, grade in zip(subjects, grades)}
print(grade_dict)

#(2) 딕셔너리에서 특정 조건을 만족하는 항목만 선택하여 새로운 딕셔너리 만들기
original_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'bam': 4, 'bae': 5}
filtered_dict = {k:v for k, v in original_dict.items() if v > 2}
print(filtered_dict)

#(3) 아래 words의 각 값을 키값으로 하고 값은 각 요소의 개수인 딕셔너리 생성
words = ['apple', 'apple', 'bae', 'bam', 'bae']
word_counts = {w:words.count(w) for w in set(words)}
print(word_counts)