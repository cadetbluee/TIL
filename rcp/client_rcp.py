## CLIENT ##

import socket
from _thread import *

HOST = '192.168.28.219' ## server에 출력되는 ip를 입력해주세요 ##
PORT = 9999 #서버의 port번호
NAME = 'cadetblue' #클라이언트 이름

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓 생성
client_socket.connect((HOST, PORT)) #서버에 연결

#서버로부터 받은 데이터 출력
def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        print(":".join(data.decode().split('\\')))

start_new_thread(recv_data, (client_socket,))
print(f'>> 서버에 연결 IP:{HOST}, PORT:{PORT}')

#서버로 데이터 전송
while True:
    message = f'[{NAME}]\\'+input()
    if message == 'quit': 
        close_data = message
        break

    client_socket.send(message.encode())

client_socket.close()