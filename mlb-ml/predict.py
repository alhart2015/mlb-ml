"""
Entry point to predict stuff.
"""
from api import gameday_api_handler

import utils

def this_is_a_test():
    return 2

def main():
    response = gameday_api_handler.get_hitter_stats(utils.HITTER_STAT_URL)
    print(response.json)

if __name__ == '__main__':
    main()