import re
import pandas as pd

PLAYER_NAME_REGEX = re.compile('> \w+.+\w+.? <')

def clean_player_name(player_name):
    match = PLAYER_NAME_REGEX.search(player_name)
    try:
        return match.group(0)[2:-2]
    except:
        print(player_name)

df = pd.read_csv('draft_data/draft.csv')

df['Name'] = df.apply(lambda row: clean_player_name(row['Player']), axis=1)

df = df.drop(columns=['Player', 'Team', 'Affiliation'])
df = df.rename(columns={'Name': 'Player', 'Round\r\n Number': 'Round Number', 'Round\r\n Pick': 'Round Pick', 'Overall\r\n Pick': 'Overall Pick'})

df[['Player', 'Round Number', 'Round Pick', 'Overall Pick', 'Year']].to_csv('draft.csv', index=False)
