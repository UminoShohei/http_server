import socket
import os
import request
import response
import file_manage


def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 8080))
    connection.listen(5)
    os.fork()
    while True:
        try:
            conn, address = connection.accept()
            pid = os.fork()
            data = conn.recv(2048)
            if data:
                req = request.RequestParser(data.decode())
                path, method, extention = req.parse_request()
                f = file_manage.File(path)
                exist = f.exist_file()
                content = b' '
                if exist:
                    content = f.open_file()
                res = response.ResponseGenerator()
                res.decied_response(
                    method=method, content=content, exist_file=exist)
                res.decied_type(extention)
                conn.send(res.generate_response())
                conn.shutdown(1)
                conn.close()
        except:
            res = response.ResponseGenerator(is_error=True)
            res.decied_response()
            hoge = res.generate_response()
            print(hoge)
            conn.send(res.generate_response())
            conn.shutdown(1)
            conn.close()
        if pid != 0:
            os.kill(pid, 9)
            print(pid)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
