from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["school_db"]

students_col = db["students"]
courses_col = db["courses"]