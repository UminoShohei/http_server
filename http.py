import socket
import os


def parse_request(request):
    req_list = request.split('\n')
    get_list = req_list[0].split(' ')
    print(req_list)
    path = get_list[1].split('/', 1)[1]
    c_type = check_type(path)
    return path, get_list[0], c_type


def exist_file(path):
    return os.path.exists(path)


def open_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    return content


def check_type(path):
    parse_path = path.split('.', 1)
    if len(parse_path) > 1:
        return parse_path[1]
    else:
        return


def create_response(message, status="200", content=b" ", c_type=None):
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
    res = b'HTTP/1.0 ' + status.encode() + b' ' + message.encode() + b'\nContent-Type: ' + content_type.encode() + \
        b'\nServer: hoge\nContent-Length: ' + \
        str(len(content)).encode() + b'\n\n' + content
    return res


def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 8080))
    connection.listen(5)
    os.fork()
    while True:
        try:
            conn, address = connection.accept()
            os.fork()
            data = conn.recv(2048)
            if data == ('close\r\n').encode('utf-8'):
                break
            elif data:
                path, method, c_type = parse_request(data.decode())
                if method != "GET" and method != "HEAD":
                    res = create_response(
                        c_type=c_type, status="405", message="Not Allowd")
                elif exist_file(path):
                    content = open_file(path)
                    if method == 'GET':
                        res = create_response(
                            content=content, c_type=c_type, message="OK")
                    elif method == 'HEAD':
                        res = create_response(c_type=c_type, message="OK")
                else:
                    res = create_response(status="404", message="Not Found")
                print(res)
                conn.send(res)
                conn.shutdown(1)
                conn.close()
                exit()
        except:
            res = create_response(
                status="500", message="Internal Server Error")
            conn.send(res)
            conn.shutdown(1)
            conn.close()
            exit()


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
