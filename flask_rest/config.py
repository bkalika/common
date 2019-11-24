import os


class Config:
    DEBUG = False
    SECRET_KEY = 'my-super-secret-key'


class TestConfig(Config):
    DEBUG = True
    SECRET_KEY = 'my-test-secret-key'


class ProdConfig(Config):
    SECRET_KEY = 'my-prod-secret-key'


def run_config():
    env = os.environ.get("ENV")
    if env == "PROD":
        return ProdConfig
    elif env == "TEST":
        return TestConfig
    else:
        return Config
