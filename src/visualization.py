import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os

def set_style():
    sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.labelsize'] = 13

def save_figure(fig, filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    figures_dir = os.path.join(base_dir, 'reports', 'figures')
    os.makedirs(figures_dir, exist_ok=True)
    filepath = os.path.join(figures_dir, f'{filename}.png')
    fig.savefig(filepath, bbox_inches='tight', dpi=150)
    print(f"Figure saved: {filepath}")

def plot_goals_by_decade(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    decade_data = df.groupby('decade')['goals_per_match'].mean().reset_index()
    sns.lineplot(data=decade_data, x='decade', y='goals_per_match', marker='o', linewidth=2.5, ax=ax)
    ax.axvline(x=1992, color='red', linestyle='--', alpha=0.5, label='Back-pass rule (1992)')
    ax.axvline(x=1994, color='orange', linestyle='--', alpha=0.5, label='3 points for win (1994)')
    ax.axvline(x=2018, color='purple', linestyle='--', alpha=0.5, label='VAR introduced (2018)')
    ax.set_xlabel('Decade')
    ax.set_ylabel('Goals per Match')
    ax.set_title('Evolution of Goals per Match Across World Cup History')
    ax.legend()
    plt.tight_layout()
    return fig

def plot_home_advantage(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    host_won_counts = df['host_won_bool'].value_counts()
    labels = ['Host did not win', 'Host won']
    colors = ['#e74c3c', '#2ecc71']
    ax.bar(labels, [host_won_counts.get(False, 0), host_won_counts.get(True, 0)], color=colors)
    for i, v in enumerate([host_won_counts.get(False, 0), host_won_counts.get(True, 0)]):
        ax.text(i, v + 0.3, str(v), ha='center', fontweight='bold')
    ax.set_ylabel('Number of Editions')
    ax.set_title('How Often Does the Host Win the World Cup?')
    plt.tight_layout()
    return fig

def plot_team_efficiency(df):
    champions = df['champion'].value_counts().reset_index()
    champions.columns = ['team', 'titles']
    appearances = pd.concat([df['champion'], df['runner_up'], df['third_place'], df['fourth_place']]).value_counts().reset_index()
    appearances.columns = ['team', 'appearances']
    merged = champions.merge(appearances, on='team', how='right').fillna(0)
    merged['titles'] = merged['titles'].astype(int)
    merged['win_rate'] = (merged['titles'] / merged['appearances'] * 100).round(1)
    fig, ax = plt.subplots(figsize=(14, 8))
    scatter = ax.scatter(
        merged['appearances'], merged['titles'],
        s=merged['win_rate'] * 10, alpha=0.6,
        c=merged['win_rate'], cmap='viridis'
    )
    for _, row in merged.iterrows():
        if row['titles'] > 0 or row['appearances'] >= 10:
            ax.annotate(row['team'], (row['appearances'], row['titles']), fontsize=9, alpha=0.8)
    ax.set_xlabel('Number of Appearances in Top 4')
    ax.set_ylabel('Number of Titles')
    ax.set_title('Team Efficiency: Appearances in Top 4 vs Titles Won')
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Win Rate (%)')
    plt.tight_layout()
    return fig

def plot_top_scorers(df):
    top10 = df[df['is_multiple'] == False].nlargest(10, 'goals')
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = sns.color_palette("viridis", 10)
    bars = ax.barh(top10['player'] + ' (' + top10['year'].astype(str) + ')', top10['goals'], color=colors)
    for i, (_, row) in enumerate(top10.iterrows()):
        ax.text(row['goals'] + 0.3, i, f"{row['goals_per_match']:.2f} g/m", va='center', fontsize=9)
    ax.set_xlabel('Goals')
    ax.set_title('Top 10 World Cup Top Scorers (with Goals per Match ratio)')
    ax.invert_yaxis()
    plt.tight_layout()
    return fig

def plot_attendance_by_country(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    country_attendance = df.groupby('host')['attendance'].sum().sort_values(ascending=True)
    ax.barh(country_attendance.index, country_attendance.values / 1_000_000, color=sns.color_palette("viridis", len(country_attendance)))
    ax.set_xlabel('Total Attendance (millions)')
    ax.set_title('Total World Cup Attendance by Host Country')
    plt.tight_layout()
    return fig
