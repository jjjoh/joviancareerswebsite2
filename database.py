

from sqlalchemy import create_engine, text
import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

connection = mysql.connector.connect(
  host= os.getenv("DB_HOST"),
  user=os.getenv("DB_USERNAME"),
  password= os.getenv("DB_PASSWORD"),
  database= os.getenv("DB_NAME"),
  ssl_verify_identity=True,
  ssl_ca='secret_url'
)


connection_string = str(connection) 

engine = create_engine(
    "mysql+pymysql://user:password@host/db?charset=utf8mb4",
    connect_args={
        "ssl":{
            "ssl_verify_identity":True,
            "ca" : "secret_url"
        }
    }
    )

#with engine.connect() as conn:
#    result = conn.execute(text("select * from jobs"))
#    print(result.all())

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row))
        return jobs       