def dec_to_bin(n):
    if n<=1:
        return str(n)
    else:
        result=dec_to_bin(n//2)+str(n%2)
    return result
def is_position_safe(N,M,current):
    directs=[(-1,0),(1,0),(0,-1),(0,1)]#(y축,x축) -> 2차원 배열 풀때 유용
    cur_r,cur_c=current
    if(0 <=cur_r+directs[M][0]<N)and(0 <=cur_c+directs[M][1]<N):
        return True
    else:
        return False
def get_final_position(N,matrix,move_list):
    directs=[(-1,0),(1,0),(0,-1),(0,1)]
    cur_r,cur_c=0,0
    for r in range(N):
        for c in range(N):
            if matrix[r][c]==1:
                cur_r,cur_c=r,c
                break #반복문 하나만 빠져나옴
        else:
            continue
        break
    for move in move_list:
        cur_r += directs[move][0]
        cur_c += directs[move][1]
        if cur_r<0 or cur_c>=N or cur_c<0 or cur_c>=N:
            return None
    return [cur_r,cur_c]