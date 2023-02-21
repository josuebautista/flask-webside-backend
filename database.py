from sqlalchemy import create_engine, text

db_string = "mysql+pymysql://40rifq6cfqip325ekzlp:pscale_pw_WqllJDnj3SOWFUDWqcu72upkwm5s47nd6LnAiJjUleI@us-east.connect.psdb.cloud/flask-webside-backend"

ssl={
    "ssl": {
        "ssl_ca": "ca.pem",
        "ssl_cert": "client-cert.pem",
        "ssl_key": "client-key.pem"
    }
}

engine = create_engine(db_string, connect_args=ssl)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    print(result.all())

