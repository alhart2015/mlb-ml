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

def add_teams_to_db(teams: List[Team], db) -> None:
    """
    Populate the teams table with the teams provided. If no table exists, this
    will make the table first. If any row is already in the table, this will
    skip that row.
    """
    cursor = db.cursor()
