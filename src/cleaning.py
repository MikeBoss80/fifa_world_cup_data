import pandas as pd
import numpy as np

TEAM_NAME_MAPPING = {
    'West Germany': 'Germany',
    'Soviet Union': 'Russia',
    'Czechoslovakia': 'Czechia',
    'Yugoslavia': 'Serbia',
    'East Germany': 'Germany',
}

def standardize_team_names(df, column):
    return df[column].replace(TEAM_NAME_MAPPING)

def add_decade_column(df, year_col='year'):
    df = df.copy()
    df['decade'] = (df[year_col] // 10) * 10
    return df

def clean_editions(df):
    df = df.copy()
    df['host_won_bool'] = df['host_won'].map({'Yes': True, 'No': False})
    df['decade'] = (df['year'] // 10) * 10
    df['attendance_per_match'] = (df['attendance'] / df['matches']).round(0).astype(int)
    df['champion'] = standardize_team_names(df, 'champion')
    df['runner_up'] = standardize_team_names(df, 'runner_up')
    df['third_place'] = standardize_team_names(df, 'third_place')
    df['fourth_place'] = standardize_team_names(df, 'fourth_place')
    return df

def clean_matches(df):
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['total_goals'] = df['score1'] + df['score2']
    df['goal_diff'] = abs(df['score1'] - df['score2'])
    knockout_stages = ['Round of 16', 'Round of 32', 'Quarter-final', 'Semi-final', 'Final', '3rd Place', 'Final Round']
    df['is_knockout'] = df['stage'].isin(knockout_stages)
    df['is_group_stage'] = df['stage'].str.contains('Group', case=False, na=False)
    upset_keywords = ['upset', 'shock', 'sorpresa']
    df['is_upset'] = df['notes'].str.contains('|'.join(upset_keywords), case=False, na=False)
    df['has_extra_time'] = df['notes'].str.contains('AET', case=False, na=False)
    df['has_penalties'] = df['notes'].str.contains('pens|penalties', case=False, na=False)
    df['is_record'] = df['notes'].str.contains('record|first|biggest|highest', case=False, na=False)
    df['team1'] = standardize_team_names(df, 'team1')
    df['team2'] = standardize_team_names(df, 'team2')
    return df

def clean_top_scorers(df):
    df = df.copy()
    df['goals_per_match'] = (df['goals'] / df['matches_played']).round(2)
    df['champion_scorer'] = df['team_result'] == 'Champions'
    df['is_multiple'] = df['player'] == 'Multiple Winners'
    df['decade'] = (df['year'] // 10) * 10
    df['country'] = standardize_team_names(df, 'country')
    return df

def clean_2026_teams(df):
    df = df.copy()
    df['is_debutant'] = df['debut_2026'] == 'Yes'
    df['is_champion'] = df['best_wc_result'].str.contains('Winners', case=False, na=False)
    result_map = {
        'First appearance': 0,
        'Group stage': 1,
        'Round of 16': 2,
        'Quarter-finals': 3,
        'Semi-finals': 4,
        'Runner-up': 5,
        'Winners': 6,
    }
    def map_result(val):
        for key, num in result_map.items():
            if key.lower() in str(val).lower():
                return num
        return 1
    df['best_round_numeric'] = df['best_wc_result'].apply(map_result)
    def rank_category(rank):
        if rank <= 10:
            return 'Elite'
        elif rank <= 30:
            return 'High'
        elif rank <= 60:
            return 'Medium'
        else:
            return 'Low'
    df['fifa_rank_category'] = df['fifa_rank'].apply(rank_category)
    return df

def clean_2026_fixtures(df):
    df = df.copy()
    df['is_group_stage'] = df['stage'] == 'Group Stage'
    df['is_knockout'] = df['stage'] != 'Group Stage'
    return df

def clean_matches(df):
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['total_goals'] = df['score1'] + df['score2']
    df['goal_diff'] = abs(df['score1'] - df['score2'])
    knockout_stages = ['Round of 16', 'Round of 32', 'Quarter-final', 'Semi-final', 'Final', '3rd Place', 'Final Round']
    df['is_knockout'] = df['stage'].isin(knockout_stages)
    df['is_group_stage'] = df['stage'].str.contains('Group', case=False, na=False)
    upset_keywords = ['upset', 'shock', 'sorpresa']
    df['is_upset'] = df['notes'].str.contains('|'.join(upset_keywords), case=False, na=False)
    df['has_extra_time'] = df['notes'].str.contains('AET', case=False, na=False)
    df['has_penalties'] = df['notes'].str.contains('pens|penalties', case=False, na=False)
    df['is_record'] = df['notes'].str.contains('record|first|biggest|highest', case=False, na=False)
    df['team1'] = standardize_team_names(df, 'team1')
    df['team2'] = standardize_team_names(df, 'team2')
    return df

def clean_top_scorers(df):
    df = df.copy()
    df['goals_per_match'] = (df['goals'] / df['matches_played']).round(2)
    df['champion_scorer'] = df['team_result'] == 'Champions'
    df['is_multiple'] = df['player'] == 'Multiple Winners'
    df['decade'] = (df['year'] // 10) * 10
    df['country'] = standardize_team_names(df, 'country')
    return df

def clean_2026_teams(df):
    df = df.copy()
    df['is_debutant'] = df['debut_2026'] == 'Yes'
    df['is_champion'] = df['best_wc_result'].str.contains('Winners', case=False, na=False)
    result_map = {
        'First appearance': 0,
        'Group stage': 1,
        'Round of 16': 2,
        'Quarter-finals': 3,
        'Semi-finals': 4,
        'Runner-up': 5,
        'Winners': 6,
    }
    def map_result(val):
        for key, num in result_map.items():
            if key.lower() in str(val).lower():
                return num
        return 1
    df['best_round_numeric'] = df['best_wc_result'].apply(map_result)
    def rank_category(rank):
        if rank <= 10:
            return 'Elite'
        elif rank <= 30:
            return 'High'
        elif rank <= 60:
            return 'Medium'
        else:
            return 'Low'
    df['fifa_rank_category'] = df['fifa_rank'].apply(rank_category)
    return df

def clean_2026_fixtures(df):
    df = df.copy()
    df['is_group_stage'] = df['stage'] == 'Group Stage'
    df['is_knockout'] = df['stage'] != 'Group Stage'
    return df
