import unittest
import response


class TestResponse(unittest.TestCase):
    def setUp(self):
        self.response = response.ResponseGenerator()

    def test_decied_response_get_ok(self):
        method = "GET"
        exist_file = True
        content = b'<h1> hello world! </h1>'
        self.response.decied_response(method, exist_file, content)
        status = "200"
        message = "OK"
        self.assertEqual(status, self.response.status)
        self.assertEqual(message, self.response.message)
        self.assertEqual(content, self.response.content)

    def test_decied_response_head_ok(self):
        method = "HEAD"
        exist_file = True
        content = b'<h1> hello world! </h1>'
        self.response.decied_response(method, exist_file, content)
        status = "200"
        message = "OK"
        self.assertEqual(status, self.response.status)
        self.assertEqual(message, self.response.message)
        self.assertEqual(content, self.response.content)

    def test_decied_response_post_not_allowed(self):
        method = "POST"
        exist_file = True
        content = b' '
        self.response.decied_response(method, exist_file, content)
        status = "405"
        message = "Not Allowed"
        self.assertEqual(status, self.response.status)
        self.assertEqual(message, self.response.message)
        self.assertEqual(content, self.response.content)

    def test_decied_response_get_not_found(self):
        method = "GET"
        exist_file = False
        content = b' '
        self.response.decied_response(method, exist_file, content)
        status = "404"
        message = "Not Found"
        self.assertEqual(status, self.response.status)
        self.assertEqual(message, self.response.message)
        self.assertEqual(content, self.response.content)

    def test_decied_response_get_internal_server_error(self):
        content = b' '
        self.response.decied_response(is_error=True)
        status = "500"
        message = "Internal Server Error"
        self.assertEqual(status, self.response.status)
        self.assertEqual(message, self.response.message)
        self.assertEqual(content, self.response.content)

    def test_decied_type_html(self):
        extention = "html"
        self.response.decied_type(extention)
        self.assertEqual("text/html", self.response.content_type)

    def test_decied_type_css(self):
        extention = "css"
        self.response.decied_type(extention)
        self.assertEqual("text/css", self.response.content_type)

    def test_decied_type_jpg(self):
        extention = "jpg"
        self.response.decied_type(extention)
        self.assertEqual("image/jpeg", self.response.content_type)

    def test_decied_type_jpeg(self):
        extention = "jpeg"
        self.response.decied_type(extention)
        self.assertEqual("image/jpeg", self.response.content_type)

    def test_decied_type_png(self):
        extention = "png"
        self.response.decied_type(extention)
        self.assertEqual("image/png", self.response.content_type)

    def test_decied_type_js(self):
        extention = "js"
        self.response.decied_type(extention)
        self.assertEqual("application/javascript", self.response.content_type)

    def test_generate_response(self):
        self.response.status = "200"
        self.response.message = "OK"
        self.response.content_type = "text/html"
        self.response.content = b'<h1> Hello World! </h1>'
        self.response.generate_response()
        res = b'''HTTP/1.0 200 OK\nContent-Type: text/html\nServer: hoge\nContent-Length: 23\n\n<h1> Hello World! </h1>'''
        self.assertEqual(res, self.response.generate_response())


if __name__ == "__main__":
    unittest.main()
