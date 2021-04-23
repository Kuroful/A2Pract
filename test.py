import unittest
from app import app

class TestSum(unittest.TestCase):

  def test_response1(self):
    tester = app.test_client(self)
    response = tester.get('/')
    statuscode = response.status_code
    self.assertEqual(statuscode, 200)
        
  def test_response2(self):
    tester = app.test_client(self)
    response = tester.get('/yes')
    statuscode = response.status_code
    self.assertEqual(statuscode, 200)
    
if __name__ == '__main__':
  unittest.main()
