from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config.settings import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "sslmode": "require",  # obrigatório no Supabase
        "options": "-4"        # força IPv4 em alguns ambientes
    },
    future=True
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

Base.metadata.create_all(engine)