from poisson_model import predictions

def implied_probability(odds):
    return 1 / odds

# Example bookmaker odds for Lewandowski shots
bookie_odds = {"Over 3.5 Shots": 2.10, "Under 3.5 Shots": 1.70}
implied_probs = {bet: implied_probability(odds) for bet, odds in bookie_odds.items()}

# Find value bets
value_bets = []
for player, probs in predictions.items():
    model_prob_over = sum(probs[sh] for sh in range(4, 8))
    model_prob_under = 1 - model_prob_over

    if model_prob_over > implied_probs["Over 3.5 Shots"]:
        value_bets.append((player, "Over 3.5 Shots", model_prob_over, bookie_odds["Over 3.5 Shots"]))
    elif model_prob_under > implied_probs["Under 3.5 Shots"]:
        value_bets.append((player, "Under 3.5 Shots", model_prob_under, bookie_odds["Under 3.5 Shots"]))

# Print value bets
for bet in value_bets:
    print(f"VALUE BET: {bet[0]} {bet[1]} (Model: {bet[2]:.2f}, Bookmaker: {1/bookie_odds[bet[1]]:.2f})")
