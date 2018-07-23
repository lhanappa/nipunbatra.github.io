import pandas as pd


NUM_COLUMNS = 4
df = pd.read_csv("schedule.csv")
df_cols = df.columns[:NUM_COLUMNS]
html_table = df[df_cols].to_html()

with open('index.html','r') as f:
    s = f.read()
    
from bs4 import BeautifulSoup
soup = BeautifulSoup(s,'html.parser')
soup.find("div", {"id": "schedule"}).string=""
soup.find("div", {"id": "schedule"}).append(BeautifulSoup(html_table, 'html.parser'))

with open('index.html','w') as f:
    f.write(str(soup.prettify()))