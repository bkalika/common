class Config:
    DEBUG = False
    SECRET_KEY = 'my-super-secret-key'


class TestConfig(Config):
    DEBUG = True
    SECRET_KEY = 'my-test-secret-key'


class ProdConfig(Config):
    SECRET_KEY = 'my-prod-secret-key'


def get_config(env):
    return configs.get(env, Config)


configs = {
    "PROD": ProdConfig,
    "TEST": TestConfig
}
