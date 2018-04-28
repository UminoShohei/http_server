import socket
import os


def response():
    html = '<h1> helloworld </h1>'
    res = 'HTTP/1.0 200 OK\n\
Content-Type: text/html\n\
Server: hoge\n\
Content-Length: ' + str(len(html)) + '\n\
\n\
' + html + '\n'
    return res


def parse_request(request):
    req_list = request.split('\n')
    get_list = req_list[0].split(' ')
    return get_list[1].split('/', 1)[1]


def open_file(path):
    type = check_type(path)
    f = open(path)
    content = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
    return content, type


def check_type(path):
    parse_path = path.split('.', 1)
    return parse_path[1]


def create_response(content, type):
    if type == 'html':
        content_type = 'type/html'
    elif type == 'css':
        content_type = 'type/css'
    elif type == 'jpg' | | type == 'jpeg':
        content_type = 'image/jpeg'
    elif type == 'png':
        content_type = 'image/png'
    elif type == 'js':
        content_type = 'application/javascript'
    res = 'HTTP/1.0 200 OK\n\
Content-Type: ' + type + '\n\
Server: hoge\n\
Content-Length: ' + str(len(content)) + '\n\
\n\
' + content + '\n'
    return res


def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 8080))
    connection.listen(5)
    os.fork()
    while True:
        conn, address = connection.accept()
        os.fork()
        data = conn.recv(2048)
        print(data)
        if data == ('close\r\n').encode('utf-8'):
            break
        elif data:
            path = parse_request(data.decode())
            print(path)
            content = open_file(path)
            res = create_response(content, type)
            conn.send(res.encode())
            conn.shutdown(1)
            conn.close()
            exit()


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
