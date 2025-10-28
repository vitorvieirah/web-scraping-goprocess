from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config.settings import DATABASE_URL

import os
import psycopg2.extensions
import socket

def force_ipv4():
    old_getaddrinfo = socket.getaddrinfo

    def new_getaddrinfo(*args, **kwargs):
        responses = old_getaddrinfo(*args, **kwargs)
        ipv4_only = [r for r in responses if r[0] == socket.AF_INET]
        return ipv4_only or responses  # fallback para o original se não houver IPv4
    socket.getaddrinfo = new_getaddrinfo

force_ipv4()

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()