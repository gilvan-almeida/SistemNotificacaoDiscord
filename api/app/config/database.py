import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("Error no url DataBase")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping = True,
)

sessionLocal = sessionmaker(
    bind = engine,
    autocommit = False,
    autoflush = True,
)



Base = declarative_base()