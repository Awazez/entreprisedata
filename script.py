import pandas as pd
import numpy as np

df = pd.read_csv('file_01.csv')

df = df[df.etatAdministratifEtablissement != "F"]
df.to_csv("file_final.csv", sep='\t', encoding='utf-8')




