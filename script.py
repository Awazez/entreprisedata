import pandas as pd
import numpy as np
import os
import s3fs

import pyarrow as pa
from pyarrow import csv

# Create filesystem object
S3_ENDPOINT_URL = "https://" + os.environ["AWS_S3_ENDPOINT"]
fs = s3fs.S3FileSystem(client_kwargs={'endpoint_url': S3_ENDPOINT_URL})


BUCKET_OUT = "<mon_bucket>"
FILE_KEY_OUT_S3 = "mon_dossier/BPE_ENS.csv"
FILE_PATH_OUT_S3 = BUCKET_OUT + "/" + FILE_KEY_OUT_S3

with fs.open(FILE_PATH_OUT_S3, 'w') as file_out:
    df_bpe.to_csv(file_out)


DATA = []

#déonmination, adresse, NAF, forme juridique, siren, siret, ess, N°RNA

#dénomination sociale = nom porté par la société 

#adresse = adresse de l'entreprise 

#NAF (Nomenclature d'activité Française) Le code NAF est également attribué par l'insee dans le but 
#de c




table = csv.read_csv('file_00.csv')
table = table[table.etatAdministratifEtablissement != "F"]


print(table)




#df = pd.read_csv('file_01.csv')
#df = df[df.etatAdministratifEtablissement != "F"]
#df.to_csv("file_final.csv", sep='\t', encoding='utf-8')




