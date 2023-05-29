import unittest
from lesson_11.lesson_11 import MyStr, User


class TestUnitTest(unittest.TestCase):

    def setUp(self):
        self.bot = MyStr('Nikita')
        self.first_user = User('Nikita')
        self.second_user = User('NIKITA')

    def test_mystr(self):
        self.assertEqual(str(self.bot), 'NIKITA')

    def test_user(self):
        self.assertEqual(self.first_user, self.second_user)


if __name__ == '__main__':
    unittest.main()
