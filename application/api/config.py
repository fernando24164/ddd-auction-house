import os
from pathlib import Path

from dotenv import load_dotenv


base_dir = Path.cwd()
load_dotenv(dotenv_path=str(base_dir))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "99ee020c-a872")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

key = Config.SECRET_KEY