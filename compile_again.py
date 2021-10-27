import pandas as pd

df = pd.read_csv('data.csv')
draft_df = pd.read_csv('draft.csv')
all_rookie_df = pd.read_csv('all-rookie_awards.csv')

draft_df = draft_df[draft_df['Player'].isin(df['Player'])]
df = df.merge(draft_df[['Player', 'Overall Pick']], on='Player')
df['All Rookie Team'] = df['Player'].isin(all_rookie_df['Player'])

df.to_csv('improved data.csv', index=False)
