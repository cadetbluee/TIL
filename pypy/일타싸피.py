#%%

import math

balls = {0: [3, 3], 1: [1, 5]} 

#balls[0][0]: #흰 공의 X좌표
#balls[0][1]: #흰 공의 Y좌표
#balls[1][0]: #1번 공의 X좌표
#balls[1][1]: #1번 공의 y좌표
# 0이 x좌표 , 1이 y좌표

print('1번공 y좌표:', balls[1][1])


# 1. 세기 구하기 power
power_pitago = math.sqrt((balls[0][0]-balls[1][0])**2 + (balls[0][1]-balls[1][1])**2)*40
# power = math.sqrt(power_pitago)*40
print('공 세기',power_pitago)


# 2-1 거리비율 tan = y/x 구하기
x = abs(balls[1][0] - balls[0][0])
y = abs(balls[1][1] - balls[0][1])

biyul = x/y   #거리비율을 구했다!!!!

# 2-2. 각도 구하기
radian = math.atan(biyul)
print('라디안', math.atan(biyul))
gakdo = math.degrees(radian)
print('1사분면 기준 각도', gakdo)

# 2-3. 사분면 생각한 각도 디테일
target_x = balls[1][0] - balls[0][0]
target_y = balls[1][1] - balls[0][1]

if target_x >= 0 and target_y >= 0:
    print('최종 각도',gakdo)
elif target_x >= 0 and target_y < 0:
    print('최종 각도',gakdo+90)
elif target_x < 0 and target_y < 0:
    print('최종 각도',gakdo+180) 
else:
    print('최종 각도',gakdo + 270)   



#%%

import math

def calculate_direct_shot(cue_ball_pos, target_ball_pos, pocket_pos, ball_radius):
    # 적구와 포켓 사이의 직선 거리 계산
    direct_distance = math.sqrt((pocket_pos[0] - target_ball_pos[0])**2 + (pocket_pos[1] - target_ball_pos[1])**2)
    
    # 쿠션에 부딪히지 않고 직접 포켓에 들어가기 위해 적구를 칠 위치의 오차를 계산
    error_margin = ball_radius * (direct_distance / (direct_distance + ball_radius))
    
    # 내공이 적구를 직접 치는 각도 계산
    theta = math.atan2((target_ball_pos[1] - cue_ball_pos[1]), (target_ball_pos[0] - cue_ball_pos[0]))
    
    # 오차를 감안한 적구의 타격 위치 계산
    target_hit_x = target_ball_pos[0] + error_margin * math.cos(theta)
    target_hit_y = target_ball_pos[1] + error_margin * math.sin(theta)
    
    # 내공에서 오차를 감안한 타격 위치까지의 최종 각도 계산
    final_theta = math.atan2((target_hit_y - cue_ball_pos[1]), (target_hit_x - cue_ball_pos[0]))
    
    return math.degrees(final_theta)

# 공의 반지름 (공의 지름을 반지름으로 변환)
ball_radius = 5.37 / 2

# 위치 설정: 내공 (60, 60), 적구 (190, 65), 포켓 (254, 127)
cue_ball_position = (60, 60)
target_ball_position = (190, 65)
pocket_position = (254, 127)

# 타격 각도 계산
shot_angle = 90-calculate_direct_shot(cue_ball_position, target_ball_position, pocket_position, ball_radius)
print(f"내공에서 적구를 직접 치는 각도: {shot_angle:.2f}도")

ball_radius = 5.37 / 2

# 위치 설정: 내공 (60, 60), 적구 (190, 65), 포켓 (254, 127)
cue_ball_position = (60, 60)
target_ball_position = (20, 20)
pocket_position = (0, 0)

# 타격 각도 계산
shot_angle = 90-calculate_direct_shot(cue_ball_position, target_ball_position, pocket_position, ball_radius)
print(f"내공에서 적구를 직접 치는 각도: {shot_angle:.2f}도")

ball_radius = 5.37 / 2

# 위치 설정: 내공 (60, 60), 적구 (190, 65), 포켓 (254, 127)
cue_ball_position = (60, 60)
target_ball_position = (20, 100)
pocket_position = (0, 127)

# 타격 각도 계산
shot_angle = calculate_direct_shot(cue_ball_position, target_ball_position, pocket_position, ball_radius)
print(f"내공에서 적구를 직접 치는 각도: {shot_angle:.2f}도")

ball_radius = 5.37 / 2

# 위치 설정: 내공 (60, 60), 적구 (190, 65), 포켓 (254, 127)
cue_ball_position = (60, 60)
target_ball_position = (200, 20)
pocket_position = (254, 0)

# 타격 각도 계산
shot_angle = calculate_direct_shot(cue_ball_position, target_ball_position, pocket_position, ball_radius)
print(f"내공에서 적구를 직접 치는 각도: {shot_angle:.2f}도")

# %%
import math

balls = {0: [3, 3], 1: [5, 1]} 

#balls[0][0]: #흰 공의 X좌표
#balls[0][1]: #흰 공의 Y좌표
#balls[1][0]: #1번 공의 X좌표
#balls[1][1]: #1번 공의 y좌표
# 0이 x좌표 , 1이 y좌표


# 1. 세기 구하기
power_pitago = math.sqrt((balls[0][0] - balls[1][0])**2 + (balls[0][1] - balls[1][1])**2) # 거리
power = power_pitago*1 # 힘 세기 

# 2. 각도 구하기
# radian = math.atan2(target_y - white_y, target_x - white_x)
radian = math.atan2(balls[1][0] - balls[0][0],balls[1][1] - balls[0][1])
gakdo = math.degrees(radian)
print(gakdo)


r=5.37 / 2
hole=[(0,0),(0,127),(127,0),(127,127),(254,0),(254,127)]
min_hole=381
for i in hole:
    m=(i[0]-balls[1][0])+(i[1]-balls[1][1])
    if m<min_hole:
        min_hole=m
        my_hole=(i[0],i[1])

a = math.sqrt((abs(balls[0][0] - my_hole[0]))**2 + (abs(balls[0][1] - my_hole[1]))**2)
b=math.sqrt((abs(my_hole[0] - balls[1][0]))**2 + (abs(my_hole[1] - balls[1][1]))**2)
c=math.sqrt((abs(balls[0][0] - balls[1][0]))**2 + (abs(balls[0][1] - balls[1][1]))**2)
rad_1=math.atan2(balls[0][0] - my_hole[0],balls[0][1] - my_hole[1])
rad_1=math.atan2(3-0,3-0)
print(rad_1)
cos_3=(a**2+b**2-c**2)/(2*a*b)
print(math.degrees(90-rad_1))
d=math.sqrt(a**2+(b+2*r)**2-2*a*(b+2*r)*cos_3)
print((a**2+d**2-(b+2*r)**2)/(2*a*d))
ran_2=math.acos((a**2+d**2-(b+2*r)**2)/(2*a*d))
print(math.degrees(rad_1)+math.degrees(ran_2))
# %%
