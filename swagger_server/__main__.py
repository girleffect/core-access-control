#!/usr/bin/env python3

import connexion

from flask_sqlalchemy import SQLAlchemy
from raven import Client
from raven.contrib.flask import Sentry

from ge_core_shared import decorators, exception_handlers, middleware
from project import settings
from project.errors import errors
from prometheus_client import make_wsgi_app
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.wsgi import DispatcherMiddleware

from swagger_server import encoder
from swagger_server.controllers import access_control_controller, operational_controller
from swagger_server.controllers import controller_validators

DB = SQLAlchemy()

metrics = decorators.MetricDecoration(
    [access_control_controller, operational_controller], "core_access_control")
metrics.decorate_all_in_modules()

# We create and set up the app variable in the global context as it is used by uwsgi.
app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Access Control API'}, strict_validation=True)

app.app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI
app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

app.add_error_handler(SQLAlchemyError, exception_handlers.db_exceptions)
app.add_error_handler(
    controller_validators.InvalidRequest, controller_validators.handle_invalid_request
)
app.app.register_blueprint(errors)

# Register middleware
middleware.metric_middleware(app.app, "core_access_control")
middleware.auth_middleware(app.app, "core_access_control")

DB.init_app(app.app)
CLIENT = Client(
    dsn=settings.SENTRY_DSN,
    processors=(
        "project.processors.SanitizeHeadersProcessor",
    ),
    extra={
        "app": app.app,
    }
)
SENTRY = Sentry(client=CLIENT)
SENTRY.init_app(app.app, level=settings.SENTRY_LOG_LEVEL)
app.app = DispatcherMiddleware(app.app, {
    "/metrics": make_wsgi_app()
})

if __name__ == '__main__':
    app.run(port=8080)
