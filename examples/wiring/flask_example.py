"""Flask wiring example."""

import sys

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide
from flask import Flask, json


class Service:
    ...


class Container(containers.DeclarativeContainer):

    service = providers.Factory(Service)


def index_view(service: Service = Provide[Container.service]) -> str:
    return json.dumps({'service_id': id(service)})


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    app = Flask(__name__)
    app.add_url_rule('/', 'index', index_view)
    app.run()
