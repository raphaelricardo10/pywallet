import unittest
from database import Database

class TestDatabase(unittest.TestCase):

    def test_connection(self):
        database = Database('pywallet')
        self.assertNotEqual(database.connection, None)

    def test_connection_error(self):
        # It is needed to implement a network-blocking method before
        with self.assertRaises(ConnectionError):
            Database('pywallet')

    def test_wrong_db_name(self):
        with self.assertRaises(ValueError):
            Database('wrong-db-name')