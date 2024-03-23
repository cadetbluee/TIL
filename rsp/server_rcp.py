## SERVER ##

import socket
from _thread import *

client_sockets = []

## 서버의 IP 및 PORT번호 지정 ##
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

########## 클라이언트 1개의 요청을 처리하는 쓰레드 ##
def threaded(client_socket, addr):
    print('>> 클라이언트 연결 :', addr[0], ':', addr[1])

    ## 클라이언트에 데이터 전송 ##
    while True:
        try:
            #클라이언트로 부터 입력 받도록 대기
            data = client_socket.recv(1024)

            #클라이언트 연결 종료
            if not data: 
                print('>> 클라이언트 연결 종료 ' + addr[0], ':', addr[1])
                break

            print('>> Received from ' + addr[0], ':', addr[1], data.decode())

            #모든 클라이언트에게 메시지 전송 (자신 제외)
            for client in client_sockets:
                if client != client_socket:
                    client.send(data)
        
        except ConnectionResetError as e:  #소켓 연결이 예기치 않게 닫혔을 때 발생하는 에러
            print('>> 클라이언트 연결 종료 ' + addr[0], ':', addr[1])
            break
        
    #종료된 클라이언트 소켓 리스트에서 제거
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print('남은 클라이언트 수 : ', len(client_sockets))

    client_socket.close()

############# 서버 소켓 생성 및 바인딩 ##
print('>> 서버 시작 :', HOST)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET: IPv4 주소 체계, SOCK_STREAM:TCP
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #함수는 소켓 옵션을 설정 (프로그램 종료된 후에도 해당 HOST및 PORT재사용)
server_socket.bind((HOST, PORT)) #서버 소켓을 특정 주소와 포트에 바인딩
server_socket.listen() #클라이언트의 연결을 기다리는 상태로 전환

############# 클라이언트 연결 대기 및 클라이언트 소켓 생성 ##
try:
    while True:
        print('>> 클라이언트 연결 대기')
        client_socket, addr = server_socket.accept() #클라언트 소켓, (IP, 포트)
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        print("참가자 수 : ", len(client_sockets))
except Exception as e:
    print('에러 : ', e)
finally:
    server_socket.close()