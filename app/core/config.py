import os
from dotenv import load_dotenv

load_dotenv()

# Database URL can be overridden by env; default stays SQLite for now.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./tasks.db")
