import os
from dotenv import load_dotenv

load_dotenv()

# Database URL can be overridden by env; default stays SQLite for now.
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://username:password@localhost:5432/dbname"
