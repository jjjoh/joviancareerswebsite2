

from sqlalchemy import create_engine#, text
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
  ssl_ca='C:/ssl/cacert-2023-12-12.pem'
)


connection_string = str(connection) 

url = "https://example.com?host=" + os.getenv("DB_HOST") + "&user=" + os.getenv("DB_USERNAME") + "&password=" + os.getenv("DB_PASSWORD") + "&database=" + os.getenv("DB_NAME") + "&autocommit=True&ssl_mode=VERIFY_IDENTITY&ssl_ca=/etc/ssl/cert.pem"


engine = create_engine(
    "mysql+pymysql://2sjk5ktin3xwi79i79qx:pscale_pw_GG6Y6FXzMhp1uQ2LWkahK7S2lRQWuiegWECX5uXh57x@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4",
    connect_args={
        "ssl":{
            "ssl_verify_identity":True,
            "ca" : "C:/ssl/cacert-2023-12-12.pem"
        }
    }
    )

#with engine.connect() as conn:
#    result = conn.execute(text("select * from jobs"))
#    print(result.all())

    