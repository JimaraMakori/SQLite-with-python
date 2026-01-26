import sqlite3

database = 'coding.sqlite'

conn = sqlite3.connect(database)

print("Opened database successfully")

import pandas as pd
tables = pd.read_sql ("SELECT * FROM sqlite_master WHERE type='table';", conn)

print (tables)