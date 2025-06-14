import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://petpal_user:Qu33nbear!@localhost:5432/petpal")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
