from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
import psycopg2 # Database driver
from dotenv import load_dotenv

load_dotenv() #load the env file 
app = Flask(__name__)

db = SQLAlchemy(app)

CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

app.config.from_object(Config)
from app import views, models