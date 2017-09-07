import os
from api import everything
import unittest
import tempfile

class TestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_name = tempfile.mkstemp()
        everything.app.config["TESTING"] = True
        self.app = everything.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_name)

    def test_assert(self):
        assert True

if __name__ == "__main__":
    unittest.main()