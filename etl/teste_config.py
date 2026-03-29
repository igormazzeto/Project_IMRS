import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd

# Troque o import abaixo para alternar entre local e nuvem
from config.db_local import get_engine
# from config.db_cloud import get_engine

engine = get_engine()

df = pd.read_sql("SELECT * FROM public.teste", engine)
print(df)
print("\n✅ Conexão funcionando!")