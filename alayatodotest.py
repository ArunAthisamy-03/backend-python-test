"""
Test cases for view and its services
"""
import unittest
from alayatodo import app

class TestViews(unittest.TestCase):
    """
    Our basic test class
    """

    def setUp(self):
        self.app = app.test_client()


    def test_home(self):
        """
        Test method to test home method.
        """
        response = self.app.get('/')
        self.assertEqual(response._status_code, 200)


    def test_login_GET(self):
        """
        Test method to test login GET method.
        """
        response = self.app.get('/login')
        self.assertEqual(response._status_code, 200)


    def test_login_POST_InValid(self):
        """
        Test method to test login Post method with invalid login accounts.
        """
        response = self.app.post('/login',data = dict(username="test@gmail.com", password="test"),follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_login_POST_Valid(self):
        """
        Test method to test login Post method with valid login accounts.
        """
        response = self.app.post('/login',data = dict(username="user1", password="user1"),follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_logout(self):
        """
        Test method to test logout method.
        """
        response = self.app.get('/logout',follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_todo_Get(self):
        """
        Test method to test todo get method.
        """
        response = self.app.get('/todo/1',follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_todo_Get_Invalid(self):
        """
        Test method to test todo get method with Invlaid id.
        """
        response = self.app.get('/todo/Invalid',follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_todojson_Get(self):
        """
        Test method to test todojson method.
        """
        response = self.app.get('/todo/1/json',follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_todojson_Get_Invalid(self):
        """
        Test method to test todojson method with Invalid id.
        """
        response = self.app.get('/todo/Invalid/json',follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_todos_Get(self):
        """
        Test method to test todos method.
        """
        with self.app as c:
            with c.session_transaction() as sess:
                sess['logged_in'] = True
        response = self.app.get('/todo', follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_todos_Post(self):
        """
        Test method to test todos post method.
        """
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['logged_in'] = True
                sess['user'] = 1
        response = self.app.post('/todo/',data = dict(description="mock data"), follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_tododelete_Post(self):
        """
        Test method to test todo_delete post method.
        """
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['logged_in'] = True
                sess['user'] = 1
        response = self.app.post('/todo/1',follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_todochk_Post(self):
        """
        Test method to test todochk post method.
        """
        with app.test_client() as c:
            with c.session_transaction() as sess:
                sess['logged_in'] = True
                sess['user'] = 1
        response = self.app.post('/todochk',data = dict(isChecked= 'true'),follow_redirects=True)
        self.assertEqual(response._status_code, 200)


    def test_error(self):
        """
        Test method to test error method.
        """
        response = self.app.get('/error',follow_redirects=True)
        self.assertEqual(response._status_code, 200)

if __name__ == '__main__':
    unittest.main()