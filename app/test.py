import unittest
import main
import os
import json
from dotenv import load_dotenv

load_dotenv()

class TestApi(unittest.TestCase):
    def test_api_function(self):

        os.environ['WEATHER_API_KEY'] = os.getenv('WEATHER_API_KEY')
        os.environ['MYSQL_PASS'] = os.getenv('MYSQL_PASS')
        os.environ['MYSQL_DATABASE'] = 'weather'
        os.environ['MYSQL_USER'] = 'weather'

        response = main.get_weather(use_db=True)
        test_response = json.loads(response)
        
        self.assertIsInstance(test_response, dict, '\nAPI response is not a dict')
        self.assertIn('coord', test_response, '\nNo "coord" section in API response')
        self.assertIn('main', test_response, '\nNo "main" section in API response')
        self.assertIn('wind', test_response, '\nNo "wind" section in API response')
        self.assertIn('dt', test_response, '\nNo "dt" section in API response')



if __name__ == '__main__':
    unittest.main()