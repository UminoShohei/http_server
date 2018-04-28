import socket
import os


def response():
    html = '<h1>こんにちは!</h1>'
    res = 'HTTP/1.0 200 OK\n\
Content-Type: text/html\n\
Server: hoge\n\
Content-Length: ' + str(len(html)) + '\n\
\n\
' + html + '\n'
    return res


def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 8080))
    connection.listen(5)
    os.fork()
    while True:
        conn, address = connection.accept()
        pid = os.fork()
        while True:
            data = conn.recv(2048)
            print(data)
            if data == ('close\r\n').encode('utf-8'):
                break
            elif data:
                res = response()
                conn.send(res)
        print("hoge")
        conn.shutdown(1)
        conn.close()
        exit()


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
