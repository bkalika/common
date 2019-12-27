class Config:
    TEST_VALUE = "CONFIG_VALUE"
    SECRET_KEY = 'my-super-secret-key'
    PG_USER = "bohdan"
    PG_PASSWORD = 'bohdan'
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "cursor"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI # -- don`t know what it is
    DEBUG = False


class DevConfig(Config):
    TEST_VALUE = "DEV_CONFIG_VALUE"
    DEBUG = True


class TestConfig(Config):
    TEST_VALUE = "TEST_CONFIG_VALUE"
    DEBUG = True


def get_config(env):
    return configs.get(env)


configs = {
    "TEST": TestConfig,
    "DEV": DevConfig,
    "DEFAULT": Config
}
