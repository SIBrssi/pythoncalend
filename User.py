"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""
import unittest

from Calendar import Calendar


def hash_password(password):
    return hash(password)


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = hash_password(password)
        self.calendar = Calendar(self)
        self.identifier = '@' + str(id(self))


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('test_user', 'password123')

    def test_user_functions(self):
        self.assertEqual(self.user.login, 'test_user')
        self.assertNotEqual(self.user.password, 'password123')
        self.assertIsInstance(self.user.calendar, Calendar)
        self.assertTrue(self.user.identifier.startswith('@'))

    def test_password_hashing(self):
        hashed_password = hash_password("password123")
        self.assertNotEqual(hashed_password, 'password123')
