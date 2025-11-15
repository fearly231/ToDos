import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Sprawdzamy czy jest ustawiona zmienna środowiskowa DATABASE_URL (dla Dockera)
# Jeśli nie, używamy lokalnej SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todos.db")

# Różne argumenty dla SQLite vs PostgreSQL
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()