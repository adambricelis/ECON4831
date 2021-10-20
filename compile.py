import pandas as pd

rookie_performance_df = pd.read_csv('rookie_season_performance.csv')
draft_df = pd.read_csv('draft.csv')
combine_df = pd.read_csv('combine.csv')
all_rookie_df = pd.read_csv('all-rookie_awards.csv')

rookie_performance_df['Draft Participant'] = rookie_performance_df['Player'].isin(draft_df['Player'])
rookie_performance_df['Combine Participant'] = rookie_performance_df['Player'].isin(combine_df['PLAYER'])
rookie_performance_df.loc[rookie_performance_df['Player'].isin(all_rookie_df['Player']), ['All Rookie Team']] = all_rookie_df['Award']
rookie_performance_df['All Rookie Team'].fillna('N/A', inplace=True)

rookie_performance_df.to_csv('data.csv')
