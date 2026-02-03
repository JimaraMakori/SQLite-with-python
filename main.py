import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)

print("Opened database successfully")

import pandas as pd
tables = pd.read_sql ("SELECT * FROM sqlite_master WHERE type='table';", conn)

print (tables)
teams = pd.read_sql ("""
SELECT *
FROM Team;
""",conn)
print (teams)

Matches = pd.read_sql ("""
SELECT Team_1,Team_2,Win_Margin 
FROM Match
WHERE Match_Winner == 7;
""",conn)
print (Matches)

new_teams = pd.read_sql ("""
SELECT *
FROM Team
WHERE Team_Name LIKE "P%";
""",conn)
print (new_teams)

min_max = pd.read_sql ("""
SELECT min(Win_Margin),max(Win_Margin)
FROM Match;
""",conn)
print (min_max)

min_max = pd.read_sql ("""
SELECT *
FROM Team
WHERE Team_Name LIKE "E%";
""",conn)

players_data = pd.read_sql("""
SELECT *
FROM Player
ORDER BY DOB DESC;
""", conn)
print (players_data)

players_count = pd.read_sql("""
SELECT COUNT (Player_Id),Country_Name
FROM Player 
GROUP BY Country_Name;
""", conn)
print (players_count)

result = pd.read_sql("""
SELECT SUM (Extra_Runs)
FROM Extra_Runs;
""",conn)
print (result)