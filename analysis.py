import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print("===== IPL DATA ANALYSIS =====\n")

# =========================
# BASIC INFO
# =========================
print("Total Matches Played:", len(matches))

# =========================
# TOP TEAMS
# =========================
top_teams = matches['winner'].value_counts().head()

plt.figure()
top_teams.plot(kind='bar')
plt.title("Top Winning Teams")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# TOP BATSMEN
# =========================
top_batsman = deliveries.groupby("batsman")["batsman_runs"] \
    .sum().sort_values(ascending=False).head()

plt.figure()
top_batsman.plot(kind='bar')
plt.title("Top Batsmen")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# TOP BOWLERS (WICKETS)
# =========================
wickets = deliveries[deliveries["is_wicket"] == 1]
top_bowlers = wickets["bowler"].value_counts().head()

plt.figure()
top_bowlers.plot(kind='bar')
plt.title("Top Bowlers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# BEST STRIKE RATE
# =========================
runs = deliveries.groupby("batsman")["batsman_runs"].sum()
balls = deliveries.groupby("batsman")["ball"].count()

strike_rate = (runs / balls) * 100
strike_rate = strike_rate.sort_values(ascending=False).head()

plt.figure()
strike_rate.plot(kind='bar')
plt.title("Best Strike Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n===== DONE =====")