from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert

# Caminho do .env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(BASE_DIR, "config", ".env")

load_dotenv(env_path)

# Configurações do banco
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_PORT = os.getenv("DB_PORT")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
engine = create_engine(DATABASE_URL)

# 🔹 Carrega metadata do banco
metadata = MetaData()
metadata.reflect(bind=engine)

# 🔹 Referência da tabela já existente
table = metadata.tables["stock_prices"]

def load_data():
    df = pd.read_csv("../database/actions.csv")

    # 🔹 Garantir tipo correto da data
    df["date"] = pd.to_datetime(df["date"]).dt.date

    records = df.to_dict(orient="records")

    with engine.begin() as conn:  # begin = commit automático
        for record in records:
            stmt = insert(table).values(**record)

            stmt = stmt.on_conflict_do_nothing(
                index_elements=["symbol", "date"]
            )

            conn.execute(stmt)

    print("\033[32mDados carregados com sucesso (sem duplicidade)\033[m")


if __name__ == "__main__":
    load_data()
