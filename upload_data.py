from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os
import joblib

label_encoder = joblib.load("./model/label_encoder.joblib")

load_dotenv()

df = pd.read_csv(
    "https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv?raw=true",
    sep=";",
)

# Rename columns name to lowercase
df.columns = df.columns.str.lower()

df["status_encode"] = label_encoder.transform(df["status"])

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DBNAME = os.getenv("POSTGRES_DB")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("Connection successful!")

        df.to_sql("student_performance", engine, if_exists="replace", index=False)
        print("Data loaded successfully into the 'student_performance' table.")
except Exception as e:
    print(f"Failed to connect: {e}")
