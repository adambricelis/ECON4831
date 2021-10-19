import pandas as pd

dfs = []

for year in range(0, 22):
    df = pd.read_csv(f'combine_data/{year:02d}-{year+1:02d}.csv')
    season = f'20{year:02d}-20{year+1:02d}'
    df['SEASON'] = season
    dfs.append(df)

pd.concat(dfs).to_csv('combine.csv', index=False)
