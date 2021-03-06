from flask import Flask  # из библиотеки flask импортируем КЛАСС Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config


App = Flask(__name__)
App.config.from_object(Config)
db = SQLAlchemy(App)
migrate = Migrate(App, db)
login = LoginManager(App)

from habrClone import routes, models, errors  # импортировали маршруты
