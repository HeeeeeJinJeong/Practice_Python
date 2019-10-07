import socketserver

# 생성한 소켓을 bind()함수로 IP와 포트번호를 바인딩할 때 사용됨
# HOST의 값으로 빈 문자열을 지정하면 bind()는 서버가 구동되는 컴퓨터의 IP를 자동적으로 할당함
HOST = ''
PORT = 9000


class MyTcpHandler(socketserver.BaseRequestHandler):
    # 이 클래스는 서버 하나당 단 한 번 초기화 됨
    # handle() 메소드에 클라이언트 연결 처리를 위한 로직을 구현함
    def handle(self):
        print('[%s]와 연결됨' % self.client_address[0])

        try:
            while True:
                self.data = self.request.recv(1024)
                if self.data.decode() == '/quit':
                    print('[%s] 사용자에 의해 중단' % self.client_address[0])
                    return

                print('[%s]' % self.data.decode())
                self.request.sendall(self.data)
        except Exception as e:
            print(e)


def runServer():
    print('에코 서버를 시작합니다.')
    print('에코 서버를 끝내려면 Ctrl+C를 누르세요')

    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('에코 서버를 종료합니다.')

runServer()