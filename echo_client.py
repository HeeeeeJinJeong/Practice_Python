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


def getFileFromServer(filename):
    data_transferred = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(filename.encode())

        data = sock.recv(1024)
        if not data:
            print('파일[%s]: 서버에 존재하지 않거나 전송중 오류발생' % filename)
            return

        with open('download/' + filename, 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)

    print('파일 [%s] 전송종료. 전송량 [%d]' % (filename, data_transferred))


filename = input('다운로드 받을 파일이름을 입력하세요: ')
getFileFromServer(filename)
print('클라이언트 종료')