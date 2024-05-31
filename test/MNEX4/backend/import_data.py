import pandas as pd
from sqlalchemy import create_engine

# PostgreSQLの接続情報
DATABASE_URL = "postgresql+psycopg2://your_username:your_password@your_host:your_port/your_dbname"

# SQLAlchemyのエンジンを作成
engine = create_engine(DATABASE_URL)

# Excelデータを読み込む
df = pd.read_excel('data/gasoline_prices.xlsx')

# データをPostgreSQLにインポート
df.to_sql('gasoline_prices', engine, if_exists='replace', index=False)
