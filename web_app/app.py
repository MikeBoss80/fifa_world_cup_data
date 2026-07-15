import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.visualization import (
    set_style, plot_goals_by_decade, plot_home_advantage,
    plot_team_efficiency, plot_top_scorers, save_figure
)

set_style()

st.set_page_config(
    page_title="FIFA World Cup Analysis 1930-2026",
    page_icon="🏆",
    layout="wide"
)

@st.cache_data
def load_data():
    editions = pd.read_csv('data/processed/editions_clean.csv')
    matches = pd.read_csv('data/processed/matches_clean.csv')
    top_scorers = pd.read_csv('data/processed/top_scorers_clean.csv')
    teams_2026 = pd.read_csv('data/processed/teams_2026_clean.csv')
    fixtures_2026 = pd.read_csv('data/processed/fixtures_2026_clean.csv')
    return editions, matches, top_scorers, teams_2026, fixtures_2026

editions, matches, top_scorers, teams_2026, fixtures_2026 = load_data()

st.sidebar.title("FIFA World Cup Analysis")
page = st.sidebar.radio("Navigate", [
    "Inicio", "Evolución de Goles", "Ventaja de Local",
    "Eficiencia", "Goleadores", "2026 Preview"
])

if page == "Inicio":
    st.title("FIFA World Cup Data Analysis 1930-2026")
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Editions", len(editions))
    col2.metric("Matches Analyzed", len(matches))
    col3.metric("Teams 2026", len(teams_2026))
    col4.metric("Top Scorers", len(top_scorers))
    st.markdown("---")
    st.markdown("""
    ### Análisis disponibles:
    1. **Evolución de Goles** - ¿El fútbol es más ofensivo o defensivo?
    2. **Ventaja de Local** - ¿La ventaja de local es real?
    3. **Eficiencia** - Más allá de los títulos
    4. **Goleadores** - Los artilleros históricos
    5. **2026 Preview** - Análisis del próximo mundial
    """)

elif page == "Evolución de Goles":
    st.title("Evolución de Goles por Década")
    fig = plot_goals_by_decade(editions)
    st.pyplot(fig)
    st.markdown("---")
    st.subheader("Datos por edición")
    st.dataframe(editions[['year', 'host', 'goals_per_match', 'attendance_per_match']])

elif page == "Ventaja de Local":
    st.title("Ventaja de Local")
    fig = plot_home_advantage(editions)
    st.pyplot(fig)
    st.subheader("Anfitriones que ganaron")
    host_winners = editions[editions['host_won_bool'] == True][['year', 'host', 'champion']]
    st.dataframe(host_winners)

elif page == "Eficiencia":
    st.title("Eficiencia de Selecciones")
    fig = plot_team_efficiency(editions)
    st.pyplot(fig)

elif page == "Goleadores":
    st.title("Goleadores Históricos")
    fig = plot_top_scorers(top_scorers)
    st.pyplot(fig)
    year = st.selectbox("Select year", sorted(top_scorers['year'].unique(), reverse=True))
    scorer = top_scorers[top_scorers['year'] == year]
    if len(scorer) > 0:
        st.dataframe(scorer[['player', 'country', 'goals', 'matches_played', 'goals_per_match', 'team_result']])

elif page == "2026 Preview":
    st.title("World Cup 2026 Preview")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Teams by Confederation")
        conf_counts = teams_2026['confederation'].value_counts()
        st.dataframe(conf_counts)
    with col2:
        st.subheader("Debutants")
        debutants = teams_2026[teams_2026['is_debutant'] == True]
        st.dataframe(debutants[['team', 'group', 'fifa_rank']])
    st.subheader("Average FIFA Rank by Group")
    group_rank = teams_2026.groupby('group')['fifa_rank'].mean().sort_values()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=group_rank.index, y=group_rank.values, palette='viridis', ax=ax)
    ax.set_title('Average FIFA Rank by Group - World Cup 2026')
    ax.set_xlabel('Group')
    ax.set_ylabel('Average FIFA Rank')
    ax.axhline(y=group_rank.mean(), color='red', linestyle='--', label=f'Overall avg: {group_rank.mean():.1f}')
    ax.legend()
    st.pyplot(fig)
