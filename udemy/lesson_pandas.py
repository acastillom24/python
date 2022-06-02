
import pandas as pd

LINK_DATA = 'https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/chipotle.tsv'
LINK_DATA_USER = 'https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/u.user'

# Cargamos los datos
df = pd.read_table(LINK_DATA)
dfUser = pd.read_table(LINK_DATA_USER, sep='|')

print(dfUser.shape)