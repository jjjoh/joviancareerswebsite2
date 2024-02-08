

from sqlalchemy import create_engine, text
import os
import mysql.connector

connection = mysql.connector.connect(
  host= os.getenv('DB_HOST'),
  user=os.getenv('DB_USERNAME'),
  password=os.getenv('DB_PASSWORD'),
  database=os.getenv('DB_NAME'),
  ssl_ca=os.getenv('CA')
)


#connection_string = str(connection) 
#return connection_string

engine = create_engine(
    "mysql+pymysql://"+str(connection.user)+":"+str(connection.password)+"@"+str(connection.host)+"/"+str(connection.database)+"?charset=utf8mb4",
    connect_args={
        "ssl":{
            "ca" : str(connection.ssl_ca)
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