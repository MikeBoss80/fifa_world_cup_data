# FIFA World Cup Data Analysis (1930-2026)

Análisis profundo de datos históricos de la Copa Mundial de la FIFA, respondiendo preguntas que van más allá de los típicos "top 5 países con más mundiales".

## Estructura del Proyecto

```
fifa_world_cup_data/
├── data/
│   ├── raw/                          # Datasets originales
│   │   ├── wc_all_editions.csv
│   │   ├── wc_all_matches.csv
│   │   ├── wc_top_scorers.csv
│   │   ├── wc_2026_teams.csv
│   │   └── wc_2026_fixtures.csv
│   └── processed/                    # Datos limpios (generados)
├── notebooks/                        # 8 notebooks de análisis
│   ├── 00_setup_data_pipeline.ipynb
│   ├── 01_goals_evolution.ipynb
│   ├── 02_home_advantage.ipynb
│   ├── 03_team_efficiency.ipynb
│   ├── 04_goalscorers_analysis.ipynb
│   ├── 05_confederations_rise_fall.ipynb
│   ├── 06_historical_upsets.ipynb
│   └── 07_2026_preview.ipynb
├── src/                             # Módulos Python
│   ├── data_loader.py              # Carga de datos
│   ├── cleaning.py                 # Limpieza y transformación
│   └── visualization.py            # Funciones de gráficos
├── web_app/                         # Dashboard Streamlit
│   └── app.py
├── docs/
│   └── IMPLEMENTATION_PLAN.md       # Plan detallado
├── reports/
│   └── figures/                     # Gráficos exportados
├── requirements.txt
└── README.md
