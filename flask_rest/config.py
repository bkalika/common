import os


class Config:
    SECRET_KEY = 'my-super-secret-key'
    DEBUG = True


class TestConfig:
    SECRET_KEY = 'my-test-secret-key'
    DEBUG = True


class ProdConfig:
    SECRET_KEY = 'my-prod-secret-key'
    DEBUG = False


def run_config():
    env = os.environ.get("ENV")
    if env == "PROD":
        return ProdConfig
    elif env == "TEST":
        return TestConfig
    else:
        return Config
