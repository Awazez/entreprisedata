import pandas as pd

df = pd.read_csv(products_sold.csv')

df = df[df.line_race != 0]


