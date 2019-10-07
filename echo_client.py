import socket

# 생성한 소켓을 bind()함수로 IP와 포트번호를 바인딩할 때 사용됨
# HOST의 값으로 빈 문자열을 지정하면 bind()는 서버가 구동되는 컴퓨터의 IP를 자동적으로 할당함
HOST = 'localhost'
PORT = 9000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while True:
        message = input('메시지 입력 : ')
        if message == 'Q' or 'q':
            sock.sendall(message.encode())
            break

        sock.sendall(message.encode())
        data = sock.recv(1024)
        print('[%s]' % data.decode())

print('클라이언트 종료')