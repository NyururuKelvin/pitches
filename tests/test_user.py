import unittest
from app.models import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user=User(password='nyururu')
    #tests if user password has been set to the password_hash
    def test_password(self):
        self.assertTrue(self.user.password_hash is not None)

    #tests if the password has been verfied
    def test_password_verified(self):
        self.assertTrue(self.user.verify_password('nyururu'))
    
    #tests if attribute error is raised
    def test_attribute_error_raised(self):
        with self.assertRaises(AttributeError):
            self.user.password