import pandas as pd


NUM_COLUMNS = 4
df = pd.read_csv("schedule.csv")
df_cols = df.columns[:NUM_COLUMMNS]
html_table = df[df_cols].to_html()

with open('index.html','r') as f:
    s = f.read()
    