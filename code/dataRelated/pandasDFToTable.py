import pandas as pd
import sqlite3 as db

def saveToTable(df, tableName, dbFullPath):
    con = db.connect(dbFullPath)
    df.to_sql(tableName, con, if_exists="replace")
    con.commit()
    con.close()