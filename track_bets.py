import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS bets (
        player TEXT,
        bet_type TEXT,
        odds REAL,
        stake REAL,
        result TEXT
    )
""")
conn.commit()

# Example: Logging a bet
cursor.execute("INSERT INTO bets VALUES (?, ?, ?, ?, ?)", 
               ("Lewandowski", "Over 3.5 Shots", 2.10, 10, "Win"))

conn.commit()
conn.close()
