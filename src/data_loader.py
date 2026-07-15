import os
import pandas as pd

def get_data_path(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'data', 'raw', filename)

def load_editions():
    return pd.read_csv(get_data_path('wc_all_editions.csv'))

def load_matches():
    return pd.read_csv(get_data_path('wc_all_matches.csv'))

def load_top_scorers():
    return pd.read_csv(get_data_path('wc_top_scorers.csv'))

def load_2026_teams():
    return pd.read_csv(get_data_path('wc_2026_teams.csv'))

def load_2026_fixtures():
    return pd.read_csv(get_data_path('wc_2026_fixtures.csv'))

def load_all_data():
    return {
        'editions': load_editions(),
        'matches': load_matches(),
        'top_scorers': load_top_scorers(),
        'teams_2026': load_2026_teams(),
        'fixtures_2026': load_2026_fixtures()
    }
