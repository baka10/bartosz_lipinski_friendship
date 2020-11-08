import os
from dataclasses import dataclass

basedir = os.path.abspath(os.path.dirname(__file__))


@dataclass
class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "HIDEMEWELL")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    ENV = os.getenv("ENV", "production")


class StagingConfig(BaseConfig):
    ENV = os.getenv("ENV", "staging")


class DevelopmentConfig(BaseConfig):
    ENV = os.getenv("ENV", "development")


class TestingConfig(BaseConfig):
    ENV = os.getenv("ENV", "testing")
    SQLALCHEMY_DATABASE_URI = "MOCKED"
    SQLALCHEMY_TRACK_MODIFICATIONS = "MOCKED"


STAGE_CONFIG = dict(
    dev=DevelopmentConfig,
    staging=StagingConfig,
    prod=ProductionConfig,
    test=TestingConfig,
)
stage = os.getenv("STAGE", "dev")
config = STAGE_CONFIG[stage]
