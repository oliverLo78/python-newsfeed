from os import getenv
# Helps us map the models to real MySQL tables 
from sqlalchemy.ext.declarative import declarative_base
# variable manages the overall connection to the database
from sqlalchemy import create_engine
# generates temporary connections for performing create, read, update, and delete (CRUD) operations
from sqlalchemy.orm import sessionmaker
# We used a .env file to fake the environment variable, 
# Need to first call load_dotenv() from the python-dotenv module
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()