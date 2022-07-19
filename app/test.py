import json
import os
import unittest
from time import sleep

from dotenv import load_dotenv

import main


load_dotenv()

if os.environ.get('BOOT_DELAY'):
    sleep(int(os.environ['BOOT_DELAY']))
else:
    sleep(10)


class TestApi(unittest.TestCase):
    def test_api_function(self):

        if not os.environ.get('WEATHER_API_KEY'):
            os.environ['WEATHER_API_KEY'] = os.getenv('WEATHER_API_KEY') or 'Test'

        os.environ['MYSQL_PASS'] = os.getenv('MYSQL_PASS')
        os.environ['MYSQL_DATABASE'] = 'weather'
        os.environ['MYSQL_USER'] = 'weather'

        response = main.get_weather(use_db=True)
        test_response = json.loads(response)

        self.assertIsInstance(test_response, dict, '\nAPI response is not a dict')
        self.assertIn('coord', test_response, '\nNo "coord" section in API response')
        self.assertIn('main', test_response, '\nNo "main" section in API response')
        self.assertIn('wind', test_response, '\nNo "wind" section in API response')
        # self.assertIn('cod', test_response, '\nNo "cod" section in API response')
        self.assertIn('dt', test_response, '\nNo "dt" section in API response')


if __name__ == '__main__':
    unittest.main()
