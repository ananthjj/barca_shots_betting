import requests
import sqlite3
import datetime

# FotMob Match ID (change this for each match)
MATCH_ID = "3909787"

# API URL
url = f"https://www.fotmob.com/api/matchDetails?matchId={MATCH_ID}"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
data = response.json()

# Connect to SQLite
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create table if it doesn’t exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS player_shots (
        match_id TEXT,
        player TEXT,
        team TEXT,
        shots INTEGER,
        shots_on_target INTEGER,
        minutes INTEGER,
        date TEXT
    )
""")
conn.commit()

# Extract and store player shot data
for team in data['content']['lineup']:
    for player in team['players']:
        name = player['name']
        shots = player['stats'].get('shotsTotal', 0)
        shots_on_target = player['stats'].get('shotsOnTarget', 0)
        minutes = player['stats'].get('minsPlayed', 0)
        team_name = team['team']['name']

        cursor.execute("""
            INSERT INTO player_shots (match_id, player, team, shots, shots_on_target, minutes, date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (MATCH_ID, name, team_name, shots, shots_on_target, minutes, str(datetime.date.today())))

conn.commit()
conn.close()
print("Shot data stored successfully.")
