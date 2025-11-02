word = input()
croatian_letters = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for cl in croatian_letters:
    word = word.replace(cl, "*")  # 크로아티아 문자를 하나의 임의 문자로 대체

print(len(word))  # 대체 후 남은 문자열의 길이가 곧 문자 개수