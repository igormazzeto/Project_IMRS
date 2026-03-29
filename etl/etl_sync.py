import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, inspect

load_dotenv()

# Conexões
engine_local = create_engine(os.getenv("DATABASE_LOCAL"))
engine_cloud  = create_engine(os.getenv("DATABASE_CLOUD"))

def listar_tabelas(engine):
    inspector = inspect(engine)
    return inspector.get_table_names(schema="public")

def sincronizar_tabela(tabela):
    print(f"Sincronizando tabela: {tabela}")
    df = pd.read_sql(f"SELECT * FROM public.{tabela}", engine_local)
    df.to_sql(tabela, engine_cloud, schema="public", if_exists="replace", index=False)
    print(f"{tabela} sincronizada — {len(df)} registros enviados")

def sincronizar_tudo():
    tabelas = listar_tabelas(engine_local)
    
    if not tabelas:
        print(" Nenhuma tabela encontrada no banco local.")
        return

    print(f"\ Tabelas encontradas: {tabelas}\n")
    
    for tabela in tabelas:
        sincronizar_tabela(tabela)
    
    print("\n Sincronização completa!")

if __name__ == "__main__":
    sincronizar_tudo()