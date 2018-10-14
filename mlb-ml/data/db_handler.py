"""
Manages the SQLite DB this project uses.
"""
import sqlite3

from schema.team import Team

from typing import List

DB_LOCATION = 'mlb-ml/data/sqlite_db'

TEAMS_TABLE_NAME = 'teams'
VENUES_TABLE_NAME = 'venues'
LEAGUES_TABLE_NAME = 'leagues'
DIVISIONS_TABLE_NAME = 'divisions'

CREATE_TEAMS_TABLE = '''CREATE TABLE IF NOT EXISTS teams(
    team_id             INTEGER PRIMARY KEY,
    name                TEXT,
    link                TEXT,
    team_code           TEXT,
    file_code           TEXT,
    abbreviation        TEXT,
    team_name           TEXT,
    location_name       TEXT,
    first_year_of_play  INTEGER,
    short_name          TEXT,
    active              BOOLEAN,
    venue_id            INTEGER,
    league_id           INTEGER,
    spring_league_id    INTEGER,
    division_id         INTEGER,
    sport_id            INTEGER
)'''

INSERT_TEAM_STATEMENT = '''INSERT INTO teams VALUES(
    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
)'''

CREATE_VENUE_TABLE = '''CREATE TABLE IF NOT EXISTS venues(
    venue_id    INTEGER PRIMARY KEY,
    name        TEXT,
    link        TEXT
)'''

CREATE_LEAGUE_TABLE = '''CREATE TABLE IF NOT EXISTS leagues(
    league_id   INTEGER PRIMARY KEY,
    name        TEXT,
    link        TEXT,
    is_spring   BOOLEAN
)'''

CREATE_DIVISION_TABLE = '''CREATE TABLE IF NOT EXISTS divisions(
    division_id   INTEGER PRIMARY KEY,
    name        TEXT,
    link        TEXT
)'''

CREATE_SPORT_TABLE = '''CREATE TABLE IF NOT EXISTS sports(
    sport_id   INTEGER PRIMARY KEY,
    name        TEXT,
    link        TEXT
)'''

CHECK_EXISTING_TABLES_QUERY = """SELECT name FROM sqlite_master WHERE type='table'"""

def team_fields_for_insert(team: Team) -> List:
    team_fields = [
        team.team_id,
        team.name,
        team.link,
        team.team_code,
        team.file_code,
        team.abbreviation,
        team.team_name,
        team.location_name,
        team.first_year_of_play,
        team.short_name,
        team.active,
        team.venue.venue_id,
        team.league.league_id,
        team.spring_league.league_id,
        team.division.division_id,
        team.sport.sport_id
    ]
    return team_fields

def add_teams_to_db(teams: List[Team], db) -> None:
    """
    Populate the teams table with the teams provided. If no table exists, this
    will make the table first. If any row is already in the table, this will
    skip that row.
    """
    cursor = db.cursor()

    # This'll do nothing if the table already exists
    cursor.execute(CREATE_TEAMS_TABLE)

    print(f'Adding {len(teams)} teams.')

    teams_added = 0
    teams_skipped = 0
    for team in teams:
        try:
            cursor.execute(INSERT_TEAM_STATEMENT, team_fields_for_insert(team))
            teams_added += 1
        except sqlite3.IntegrityError:
            teams_skipped += 1

    print(f'Finished adding {teams_added} teams.')
    print(f'Skipped {teams_skipped} teams.')
    print()

