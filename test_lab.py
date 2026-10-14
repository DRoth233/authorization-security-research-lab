"""Run: python -m unittest discover -v"""
import unittest
from lab import Forbidden, NotFound, secure_read, vulnerable_read

class AuthorizationTests(unittest.TestCase):
    def test_vulnerable_cross_account_read(self):
        self.assertEqual(vulnerable_read(1, 202).owner_id, 2)

    def test_secure_owner_can_read(self):
        self.assertEqual(secure_read(1, 101).owner_id, 1)

    def test_secure_cross_account_read_is_denied(self):
        with self.assertRaises(Forbidden):
            secure_read(1, 202)

    def test_unknown_record(self):
        with self.assertRaises(NotFound):
            secure_read(1, 999)

if __name__ == "__main__":
    unittest.main()
