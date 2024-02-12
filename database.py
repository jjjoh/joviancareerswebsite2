

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

try:
    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Execute "CREATE TABLE" query
    #cursor.execute("CREATE TABLE jobs(id INT NOT NULL AUTO_INCREMENT,title VARCHAR(120) NOT NULL,location VARCHAR(120) NOT NULL, salary INT,currency VARCHAR(10), responsibilities VARCHAR(2000),requirements VARCHAR(2000), create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,PRIMARY KEY (id))"
    #)

    cursor.execute("INSERT INTO jobs (title, location,salary) VALUES ('Frontend Developper','Sao Paulo','3000'), ('Backend Developper','Remote',4000)"
     )

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
  "mysql+pymysql://"+os.getenv('DATABASE_USERNAME')+":"+os.getenv('DATABASE_PASSWORD')+"@"+os.getenv('DATABASE_HOST')+"/"+os.getenv('DATABASE')+"?charset=utf8mb4",
  connect_args={"ssl":{"ca" : os.getenv('CA')}}
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