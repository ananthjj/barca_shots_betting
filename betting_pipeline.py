import os

os.system("python scripts/fotmob_scraper.py")
os.system("python betting_model/poisson_model.py")
os.system("python betting_model/value_bets.py")
os.system("python telegram_alerts.py")
