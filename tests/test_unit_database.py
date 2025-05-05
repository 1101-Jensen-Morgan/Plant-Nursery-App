import unittest
from unittest.mock import patch, MagicMock
from app import FinalProjectDatabase as db

class TestDatabaseFunctions(unittest.TestCase):

    @patch('app.FinalProjectDatabase.psycopg2.connect')
    def test_get_usernames(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('alice',), ('bob',)]
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        usernames = db.getUserNames()
        self.assertEqual(usernames, [('alice',), ('bob',)])
        mock_cursor.execute.assert_called_once_with('SELECT username FROM users')
    
    @patch('app.FinalProjectDatabase.psycopg2.connect')
    def test_get_password(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('secret123',)]
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        result = db.getPassword('bob')
        self.assertEqual(result, 'secret123')

    def test_convert_date(self):
        self.assertEqual(db.convertDate("05/01/24"), "2024-05-01")

    @patch('app.FinalProjectDatabase.getMaxID')
    def test_new_id(self, mock_maxid):
        mock_maxid.return_value = [(5,)]
        new_id = db.newID("users")
        self.assertEqual(new_id, 6)

if __name__ == '__main__':
    unittest.main()
