from sqlalchemy import create_engine, text
import os

db_string = os.getenv('DB_STRING_CONN')

ssl={
    "ssl": {
        "ssl_ca": "ca.pem",
        "ssl_cert": "client-cert.pem",
        "ssl_key": "client-key.pem"
    }
}

engine = create_engine(db_string, connect_args=ssl)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.fetchall():
            jobs.append(row._asdict())
        return jobs