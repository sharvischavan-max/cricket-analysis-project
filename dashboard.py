import pandas as pd
import streamlit as st

# =========================
# LOAD DATA
# =========================
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

st.title("🏏 IPL Data Dashboard")

# =========================
# TOP WINNING TEAMS
# =========================
st.subheader("🏆 Top Winning Teams")
top_teams = matches['winner'].value_counts().head()
st.bar_chart(top_teams)

# =========================
# TOP CITIES (FIXED)
# =========================
st.subheader("🌍 Top Cities (Matches Played)")

# Some datasets may have missing city values
top_cities = matches['city'].fillna("Unknown").value_counts().head()
st.bar_chart(top_cities)

# =========================
# TOP BATSMEN
# =========================
st.subheader("🏏 Top Batsmen")

top_batsman = deliveries.groupby("batsman")["batsman_runs"] \
    .sum() \
    .sort_values(ascending=False) \
    .head()

st.bar_chart(top_batsman)

# =========================
# TOP BOWLERS (FIXED)
# =========================
st.subheader("🔥 Top Bowlers")

# Fix for your dataset (no is_wicket column)
wickets = deliveries[deliveries["dismissal_kind"].notna()]
top_bowlers = wickets["bowler"].value_counts().head()

st.bar_chart(top_bowlers)

# =========================
# TOSS IMPACT
# =========================
st.subheader("🧠 Toss Impact")

toss_win = matches[matches['toss_winner'] == matches['winner']]
percentage = (len(toss_win) / len(matches)) * 100

st.write(f"Toss Win → Match Win %: {round(percentage,2)}%")

st.success("✅ Dashboard Loaded Successfully!")