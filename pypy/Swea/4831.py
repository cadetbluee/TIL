import sys
sys.stdin = open("4831_input.txt", "r")
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     K,N,M=map(int,input().split())
#     M_list=list(map(int,input().split()))
#     M_list.append(N)#종점을 추가해 종점으로부터 마지막 충전소도 계산
#     fuel=K #연료체크
#     stop_list=[]#리스트에 멈추는 정류장 추가
#     result=True#예외제외
#     for i in range(1,N):#정류장 0은 충전을 하니까 제외
#         fuel-=1#한칸 갈때마자 연료 소모
#         if fuel<0:#연료 모두 소진시
#             result=False#예외값에 해당
#             break#반복문 탈출
#         for stop in range(M):#충전소 하나하나 비교
#             if i==M_list[stop]:#만약 내가 충전소에 위치한다면
#                 if M_list[stop+1]-M_list[stop]>fuel:#그리고 내 연료가 다음 충전소까지 못갈 정도라면
#                     stop_list.append(M_list[stop])#리스트에 멈추는 정류장 추가
#                     fuel=K#연료 채우기
#
#     if result==True:#잘 도착했으면
#         print(f'#{test_case} {len(stop_list)}')#결과출력
#     else:#안했으면
#         print(f'#{test_case} 0')#0출력


T = int(input())  # 노선의 수

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리
for test_case in range(1, T + 1):
    # K: 한 번의 충전으로 이동할 수 있는 최대 거리
    # N: 종점까지의 총 거리
    # M: 충전소의 개수
    K, N, M = map(int, input().split())

    # 충전소의 위치를 나타내는 리스트
    charge_stop = list(map(int, input().split()))

    # 초기화
    charge_count = 0  # 충전 횟수
    current = 0  # 현재 위치

    # 종점에 도착할 때까지 반복
    while charge_count + K < N:  # 현재 위치 + 한 번 충전으로 이동 가능한 위치 < 종점
        # 현재 위치에서부터 최대 이동 거리 K만큼 감소하면서 충전소가 있는지 확인
        for i in range(K, 0, -1):  # K부터 시작해서 0 직전까지 -1 간격으로
            if (current + i) in charge_stop:
                current += i  # 충전소에 도착했으므로 해당 위치로 이동
                charge_count += 1  # 충전 횟수 증가
                break
        else:
            charge_count = 0  # 충전소가 없는 경우 충전 횟수 초기화
            break

    # 결과 출력
    print(f'#{test_case} {charge_count}')