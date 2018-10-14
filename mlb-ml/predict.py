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

    teams = gameday_api_handler.get_team_info()

    print('Connecting to SQLite DB...')
    try:
        db = sqlite3.connect(db_handler.DB_LOCATION)
    except sqlite3.OperationalError:
        raise sqlite3.OperationalError(f'Unable to open database file: {db_handler.DB_LOCATION}')
    print('Connected')
    print()

    # db_handler.add_teams_to_db(teams, db)

    players_for_nats = gameday_api_handler.get_hitter_stats_for_team_id(120, 2018, utils.REGULAR_SEASON_GAME_TYPE)
    for p in players_for_nats:
        print(p)

    print(len(players_for_nats))

    db.commit()
    db.close()


if __name__ == '__main__':
    main()