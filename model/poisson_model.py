from scipy.stats import poisson
import sqlite3
import pandas as pd

# Load player shot data
conn = sqlite3.connect("database.db")
df = pd.read_sql("SELECT player, AVG(shots) AS avg_shots FROM player_shots GROUP BY player", conn)
conn.close()

# Predict shots for next match
def poisson_prob(lmbda, shots):
    return poisson.pmf(shots, lmbda)

predictions = {}
for _, row in df.iterrows():
    player = row["player"]
    avg_shots = row["avg_shots"]
    probs = {sh: poisson_prob(avg_shots, sh) for sh in range(8)}
    predictions[player] = probs

print(predictions)  # Probability distribution of shots per player
