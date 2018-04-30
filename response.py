class ResponseGenerator:
    def __init__(self):
        self.status = ""
        self.message = ""
        self.content = ""
        self.content_type = ""

    def generate_response(self):
        res = b'HTTP/1.0 ' + self.status.encode() + b' ' + self.message.encode() + b'\nContent-Type: ' + self.content_type.encode() + \
            b'\nServer: hoge\nContent-Length: ' + \
            str(len(self.content)).encode() + b'\n\n' + self.content
        return res

    def decied_response(self,  method="GET", exist_file=True, content=b' ', is_error=False):
        self.content = content
        if is_error:
            self.status = "500"
            self.message = "Internal Server Error"
        elif method != "GET" and method != "HEAD":
            self.status = "405"
            self.message = "Not Allowed"
        elif exist_file:
            if method == 'GET':
                self.status = "200"
                self.message = "OK"
            elif method == 'HEAD':
                self.status = "200"
                self.message = "OK"
        else:
            self.status = "404"
            self.message = "Not Found"

    def decied_type(self, extention=""):
        if extention == 'html':
            self.content_type = 'text/html'
        elif extention == 'css':
            self.content_type = 'text/css'
        elif extention == 'jpg' or extention == 'jpeg':
            self.content_type = 'image/jpeg'
        elif extention == 'png':
            self.content_type = 'image/png'
        elif extention == 'js':
            self.content_type = 'application/javascript'
        else:
            self.content_type = 'text/plain'
