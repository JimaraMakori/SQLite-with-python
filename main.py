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

Join_city = pd.read_sql("""
SELECT c.Country_Id,c.Country_Name,ci.City_Name
FROM Country c
INNER JOIN City ci
ON c.Country_Id == ci.Country_id;
""",conn)

print (Join_city)

Left_Join = pd.read_sql("""
SELECT *
FROM Player
LEFT JOIN Season
ON Player.player_id == Season.Man_of_the_Series;
""",conn)

print (Left_Join)

CSK_Matches_2015 = pd.read_sql("""
SELECT Match_Id,Team_2 as Away_team,Match_Winner
FROM Match
WHERE Team_1 =
(SELECT Team_1 FROM Match WHERE Team_1 == 3 AND Season_Id == 8);
""",conn)

print (CSK_Matches_2015)