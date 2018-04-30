import unittest
import request


class TestRequest(unittest.TestCase):
    def test_parse_request_get(self):
        r = '''GET /www/html/index.html HTTP/1.1
Host: localhost:8080
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: ja,en-US;q=0.9,en;q=0.8,pt;q=0.7'''

        self.request = request.RequestParser(r)
        path, method, extention = self.request.parse_request()
        self.assertEqual("www/html/index.html", path)
        self.assertEqual("GET", method)
        self.assertEqual("html", extention)

    def test_parse_request_head(self):
        r = '''HEAD /www/html/index.html HTTP/1.1
Host: localhost:8080
User-Agent: curl/7.54.0
Accept: */*'''

        self.request = request.RequestParser(r)
        path, method, extention = self.request.parse_request()
        self.assertEqual("www/html/index.html", path)
        self.assertEqual("HEAD", method)
        self.assertEqual("html", extention)

    def test_parse_request_post(self):
        r = '''POST /www/html/sample.css HTTP/1.1
Host: localhost:8080
User-Agent: curl/7.54.0
Accept: */*'''
        self.request = request.RequestParser(r)
        path, method, extention = self.request.parse_request()
        self.assertEqual("www/html/sample.css", path)
        self.assertEqual("POST", method)
        self.assertEqual("css", extention)


if __name__ == "__main__":
    unittest.main()
