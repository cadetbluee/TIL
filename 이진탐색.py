def binary_search(arr,N,key):
    start = 0 # 구간 초기화
    end = N - 1
    while start <= end: # 검색구간이 유효하면 반복
        middle= (start+end)//2 # 중앙원소 인덱스
        if arr[middle]==key: # 검색 성공
            return middle
        elif arr[middle]>key: # 중앙값이 키보다 크면
            end=middle-1
        else:
            end=middle+1
    return -1
binary_search([1,2,3,6,7,11,12,45],8,12)

def selection_sort(a,N):
    for i in range(N-1): #구간의 시작 1, 2개의 원소가 남을 때까지
        #구간의 최솟값위치 min_idx,첫 원소를 최소로 가정
        min_idx=i
        for j in range(i+1,N): #실제 최솟값을 찾을 위치 j
            if a[min_idx]>a[j]:
                min_idx=j
        a[min_idx],a[i]=a[i],a[min_idx]
    return

N=5
arr=[-1,3,-2,5,2]
print(arr)
selection_sort(arr,N)

# %%
# 리스트 컴프리헨션 연습
# (1) 짝수만 있는 리스트 만들기
nums = [1,2,3,4,5,6,7]
even_nums = []
for n in nums :
    if n % 2 == 0 :
        even_nums.append(n)
even_nums = [n for n in nums if n % 2 == 0]

# (2) 리스트에서 음수제거 하기
nums = [-1,2,-3,-4,-5,-6,7]

# (3) 다음 숫자 리스트의 요소를 제곱한 리스트를 만들기
nums = [1,2,3,4,5,6,7]

# (4) 문자열 리스트에서 길이가 5이상인 단어만 선택
words = ['apple', 'banana', 'cherry', 'bam', 'bae']

# (5) 문자열 리스트에서 문자열의 공백이 포함된 경우 공백을 제거한 리스트 만들기
words = [' apple  ', ' banana ', ' cherry ', 'bam', 'bae     ']

# (6) 다음 학생들의 짝궁을 결정 짓기 위해 모든 짝궁의 조합을 구하시오
names = ['해인', '고은', '두홍', '봉준', '온겸']
# 아래가 출력될 수 있도록 함
# [('해인', '고은'), ('해인', '두홍'), ('해인', '봉준'), ('해인', '온겸'), ('고은', '해인'), ('고은', '두홍'), ('고은', '봉준'), ('고은', '온겸'), ('두홍', '해인'), ('두홍', '고은'), ('두홍', '봉준'), ('두홍', '온겸'), ('봉준', '해인'), ('봉준', '고은'), ('봉준', '두홍'), ('봉준', '온겸'), ('온겸', '해인'), ('온겸', '고은'), ('온겸', '두홍'), ('온겸', '봉준')]print([(n1,n2) for n1 in names for n2 in names if n1!=n2 ])

# (7) 2차원 리스트의 모든 요소를 제곱하여 새로운 2차원 리스트 생성
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
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
flatten = [e for row in matrix for e in row]
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