

from sqlalchemy import create_engine, text
import os
import mysql.connector

connection = mysql.connector.connect(
  host= "DB_HOST",
  user="DB_USERNAME",
  password="DB_PASSWORD",
  database="DB_NAME",
  ssl_verify_identity=True,
  ssl_ca="CA"
)


#connection_string = str(connection) 
#return connection_string

engine = create_engine(
    "mysql+pymysql://"+str(connection.user)+":"+str(connection.password)+"@"+str(connection.host)+"/"+str(connection.database)+"?charset=utf8mb4",
    connect_args={
        "ssl":{
            "ssl_verify_identity":True,
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