from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Update username/password/host/port/db_name as needed
DATABASE_URL = "mysql://root:password@127.0.0.1:3306/kingdom_health"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

def test_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(f"DB connection failed: {e}")
        return False
    
    