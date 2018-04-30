import os


class File:
    def __init__(self, path):
        self.path = path
        print(path)

    def exist_file(self):
        return os.path.exists(self.path)

    def open_file(self):
        with open(self.path, 'rb') as f:
            content = f.read()
        return content
