import unittest
import file_manage


class TestFile(unittest.TestCase):

    def test_exist_folder_true(self):
        path = 'www/html/index.html'
        self.file_manager = file_manage.File(path)
        self.assertEqual(True, self.file_manager.exist_file())

    def test_exist_folder_false(self):
        path = 'www/html/none.html'
        self.file_manager = file_manage.File(path)
        self.assertEqual(False, self.file_manager.exist_file())

    def test_open_file(self):
        path = 'www/html/index.html'
        self.file_manager = file_manage.File(path)
        content = b'<h1> Gundam  </h>\n'
        self.assertEqual(content, self.file_manager.open_file())


if __name__ == "__main__":
    unittest.main()
