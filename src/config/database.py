from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config.settings import DATABASE_URL
import socket
import psycopg2

def force_ipv4_connect(*args, **kwargs):
    # Força uso de IPv4 para o host do Supabase
    host = kwargs.get("host")
    if host and ":" not in host:
        # Resolve apenas o IPv4
        ipv4_addr = socket.getaddrinfo(host, None, socket.AF_INET)[0][4][0]
        kwargs["host"] = ipv4_addr
    return psycopg2.connect(*args, **kwargs)

DATABASE_URL = "postgresql+psycopg2://<user>:<password>@db.kuueonnlotjmravgavbb.supabase.co:5432/postgres"

engine = create_engine(
    DATABASE_URL,
    connect_args={"connect_factory": force_ipv4_connect},
    future=True
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()