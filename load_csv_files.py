
import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:1Lovechess@localhost/Museum database'
db = create_engine(conn_string)
conn = db.connect()

files = ['artist', 'canvas_size', 'image_link', 'museum_hours', 'museum', 'product_size', 'subject', 'work']
for file in files:
    file_path = fr'C:\Users\91863\Desktop\Museum_data\{file}.csv'
    df = pd.read_csv(file_path)
    df.to_sql(file, con=conn, if_exists='replace', index=False)