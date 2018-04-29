import socket
import os
import base64


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
    c_type = check_type(path)
    with open(path, 'rb') as f:
        content = f.read()  # ファイル終端まで全て読んだデータを返す
        # content = base64.b64encode(f.read())  # ファイル終端まで全て読んだデータを返す
    return content, c_type


def check_type(path):
    parse_path = path.split('.', 1)
    return parse_path[1]


def create_response(content, c_type):
    if c_type == 'html':
        content_type = 'text/html'
    elif c_type == 'css':
        content_type = 'text/css'
    elif c_type == 'jpg' or c_type == 'jpeg':
        content_type = 'image/jpeg'
    elif c_type == 'png':
        content_type = 'image/png'
    elif c_type == 'js':
        content_type = 'application/javascript'
    else:
        content_type = 'text/plain'

    res = b'HTTP/1.0 200 OK\nContent-Type: ' + content_type.encode() + b'\nServer: hoge\nContent-Length: ' + str(len(content)).encode() + b'\n\n' + content
    print(res)
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
        if data == ('close\r\n').encode('utf-8'):
            break
        elif data:
            path = parse_request(data.decode())
            print(path)
            content, c_type = open_file(path)
            res = create_response(content, c_type)
            conn.send(res)
            conn.shutdown(1)
            conn.close()
            exit()


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
