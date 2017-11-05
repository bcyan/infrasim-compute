#!/usr/bin/env python

from flask import Flask
from .apis import api
from .apis.qmp import ns as qmp_ns
from .apis.hmp import ns as hmp_ns
from .apis.admin import ns as admin_ns
from monitor import monitor_logger
import logging

app = Flask(__name__)

def start(instance=instance, host=host, port=port):
    api.add_namespace(qmp_ns)
    api.add_namespace(hmp_ns)
    api.add_namespace(admin_ns)

    mlog = monitor_logger.init_logger(instance)

    app.logger.addHandler(mlog)
    app.logger.setLevel(logging.DEBUG)

    app.run(host=host, port=port)
    api.init_app(app)
