"""
Entry point to predict stuff.
"""
from api import gameday_api_handler
from data import db_handler

import utils

import sqlite3

def this_is_a_test():
    return 2

def main():
    # parsed_players = gameday_api_handler.get_hitter_stats(utils.HITTER_STAT_URL)
    # for p in parsed_players:
    #     print(p)

    # print(len(parsed_players))

    teams = gameday_api_handler.get_team_info(utils.TEAM_INFO_URL)
    
    print(teams[0])
    print(vars(teams[0]))

    print('Connecting to SQLite DB...')
    try:
        db = sqlite3.connect(db_handler.DB_LOCATION)
    except sqlite3.OperationalError:
        raise sqlite3.OperationalError(f'Unable to open database file: {db_handler.DB_LOCATION}')
    print('Connected')

    db_handler.add_teams_to_db(teams, db)

    db.commit()
    db.close()


if __name__ == '__main__':
    main()