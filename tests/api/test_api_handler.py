"""
Test the api library.
"""
import unittest

from .context import predict

class ApiHandlerTest(unittest.TestCase):

    def test_pull_player_data(self):
        api_handler.pull_player_data()

def main():
    unittest.main()

if __name__ == '__main__':
    main()