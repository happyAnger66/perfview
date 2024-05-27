class Config(object):
    TESTING = False
    DCHAT_DOMAIN = "api-kylin.intra.xiaojukeji.com/snitch_openapi_online_lb"
    DCHAT_MSG_CREATE_ROUTE = "v1/message.create"
    DCHAT_BOT_ID = "99357"
    DCHAT_BOT_TYPE = "bot_user"
    DCHAT_USER = "79b7469cf48d480cae0677aa7ebb654d"
    DCHAT_PASS = "2f032f32728f4b4d92f3112abf609722"
    POSTGRESQL_CONNECTION = "/tmp/db.sqlite3"
    DB_URL="/tmp/db.sqlite3"
    PROMETHEUS_TIME_OFFSET = (-3600 * 8)

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    pass
