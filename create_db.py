import sqlite3

conn = sqlite3.connect("blackout.db") #connect to the database

cursor = conn.cursor()   #create cursor

cursor.execute("""
CREATE TABLE IF NOT EXISTS blackout_correlation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_date TEXT UNIQUE,
    loadshedding_stage INTEGER,
    total_job_postings INTEGER,
    remote_job_postings INTEGER,
    remote_percentage REAL
)
""")

conn.commit()  #save changes
conn.close()   #Close connection

print("Database created successfully.")