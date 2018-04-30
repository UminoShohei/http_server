class RequestParser:
    def __init__(self, request):
        self.request = request
        print(request)
    def parse_request(self):
        req_list = self.request.split('\n')
        get_list = req_list[0].split(' ')
        path = get_list[1].split('/', 1)[1]
        method = get_list[0]
        parse_path = path.split('.', 1)
        if len(parse_path) > 1:
            return path, method, parse_path[1]
        else:
            return path, method, ""
