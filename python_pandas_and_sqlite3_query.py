

import pandas as pd
import sqlite3

connection = sqlite3.connect("/home/user1/Desktop/db_demo_sqlite_pandas")

data=pd.read_sql_query("SELECT * FROM nba", connection)


df=pd.DataFrame(data)

print(df.head())


print("#####################################################################")
print("#####################################################################")

