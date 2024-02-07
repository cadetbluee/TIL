import sys
sys.stdin=open("4873_input.txt")
T = int(input())
for test_case in range(1, T + 1):
    S=input()
    i=0
    while i<len(S)-1:
        if S[i]==S[i+1]:
            S=S[:i]+S[i+2:]
            i=0
        else:
            i+=1
    print(f'#{test_case} {len(S)}')