import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = 'La cabra 2.0'
    USERNAME=os.getenv("USERNAME")
    HOST=os.getenv("HOST")
    DATABASE=os.getenv("DATABASE")
    PASSWORD=os.getenv("PASSWORD")
    PORT=os.getenv("PORT")