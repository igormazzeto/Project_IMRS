from sqlalchemy import create_engine, text

engine = create_engine("postgresql://igormazzeto@localhost:5432/imrs")

with engine.connect() as conn:
    conn.execute(text("SELECT 1"))

print("Conexão com o banco IMRS funcionando!")