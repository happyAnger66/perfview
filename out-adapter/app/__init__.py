import os

from flask import Flask

from .utils import log_init

def create_app(test_config=None):
    print('test_config', test_config)
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.config.from_object('app.config.ProductionConfig')
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import dchat
    from . import prometheus_proxy
    app.register_blueprint(dchat.bp)
    app.register_blueprint(prometheus_proxy.bp)
    return app


log_init('/var/log/prom_proxy.log')

app = create_app()
app.run()
