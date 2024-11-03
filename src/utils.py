from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# load the .env file variables
load_dotenv()


def db_connect():
    import os
    engine = create_engine(os.getenv('DATABASE_URL'))
    engine.connect()
    return engine

from datetime import datetime

# Define the start and end dates
start_date = datetime(2022, 11, 5)
end_date = datetime(2024, 11, 5)

# Calculate the difference in weeks
difference_in_weeks = (end_date - start_date).days // 7
difference_in_weeks
