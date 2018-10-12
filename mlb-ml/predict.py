"""
Entry point to predict stuff.
"""
from api import gameday_api_handler

import utils

def this_is_a_test():
    return 2

def main():
    this_is_a_test()
    gameday_api_handler.test()
    print(utils.HITTER_STAT_URL)


if __name__ == '__main__':
    main()