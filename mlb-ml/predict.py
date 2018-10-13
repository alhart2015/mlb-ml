"""
Entry point to predict stuff.
"""
from api import gameday_api_handler

import utils

def this_is_a_test():
    return 2

def main():
    parsed_players = gameday_api_handler.get_hitter_stats(utils.HITTER_STAT_URL)
    for p in parsed_players:
        print(p)

    print(len(parsed_players))

if __name__ == '__main__':
    main()