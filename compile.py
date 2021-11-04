import pandas as pd

df = pd.read_csv('rookie_season_performance.csv')
draft_df = pd.read_csv('draft.csv')
all_rookie_df = pd.read_csv('all-rookie_awards.csv')

draft_df = draft_df[draft_df['Year'] > 1999]
draft_df = draft_df[draft_df['Player'].isin(df['Player'])]

# Merge in All-Rookie data
df['All Rookie Team'] = df['Player'].isin(all_rookie_df['Player'])

# Merge in draft data
df = df.merge(draft_df[['Player', 'Overall Pick']], on='Player')

df.to_csv('data.csv', index=False)
