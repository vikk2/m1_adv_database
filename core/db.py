import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["school_db"]

students_col = db["students"]
courses_col = db["courses"]