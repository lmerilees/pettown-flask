# load_env.py
import os
from dotenv import load_dotenv

env = os.getenv("FLASK_ENV", "development")
load_dotenv(dotenv_path=f".env.{env}")
