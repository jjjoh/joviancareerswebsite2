

from sqlalchemy import create_engine, text
from dotenv import load_dotenv

#Load environment variablels from the .env file
load_dotenv()
import os
import MySQLdb

#Connect to the database
connection = MySQLdb.connect(
  host= os.getenv('DATABASE_HOST'),
  user=os.getenv('DATABASE_USERNAME'),
  password=os.getenv('DATABASE_PASSWORD'),
  db=os.getenv('DATABASE'),
  autocommit=True,
  ssl_mode='VERIFY_IDENTITY',
  ssl={'ca': str(os.getenv('CA'))}
)

engine = create_engine(
  "mysql+pymysql://"+os.getenv('DATABASE_USERNAME')+":"+os.getenv('DATABASE_PASSWORD')+"@"+os.getenv('DATABASE_HOST')+"/"+os.getenv('DATABASE')+"?charset=utf8mb4",
  connect_args={"ssl":{"ca" : os.getenv('CA')}}
)


#load all the datas from the jobs table
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.mappings().all():
            jobs.append(dict(row))
        return jobs

  
    
