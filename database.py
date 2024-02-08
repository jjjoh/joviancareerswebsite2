

from sqlalchemy import create_engine, text
from dotenv import load_dotenv

#Load environment variablels from the .env file
load_dotenv
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

try:
    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Execute "SHOW TABLES" query
    cursor.execute("SHOW TABLES")

    # Fetch all the rows
    tables = cursor.fetchall()

    # Print out the tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

except MySQLdb.Error as e:
    print("MySQL Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
#connection_string = str(connection) 
#return connection_string

engine = create_engine(
  "mysql+pymysql://"+str(connection.user)+":"+str(connection.password)+"@"+str(connection.host)+"/"+str(connection.db)+"?charset=utf8mb4",
  connect_args={"ssl":{"ca" : str(connection.ssl)}}
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