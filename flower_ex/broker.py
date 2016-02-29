#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TODO: File Comment
"""


from __future__ import absolute_import

import logging

from tornado import web
from tornado import gen

from flower.views import BaseHandler
from flower.utils.broker import Broker
from flower.api.control import ControlHandler


logger = logging.getLogger(__name__)


class BrokerInfo(BaseHandler):
    @web.authenticated
    @gen.coroutine
    def get(self):
        app = self.application
        broker_options = self.capp.conf.BROKER_TRANSPORT_OPTIONS

        http_api = None
        if app.transport == 'amqp' and app.options.broker_api:
            http_api = app.options.broker_api

        try:
            broker = Broker(app.capp.connection().as_uri(include_password=True),
                            http_api=http_api, broker_options=broker_options)
        except NotImplementedError:
            raise web.HTTPError(
                404, "'%s' broker is not supported" % app.transport)

        queue_names = ControlHandler.get_active_queue_names()

        if not queue_names:
            queue_names = set([self.capp.conf.CELERY_DEFAULT_QUEUE])

        queues = yield broker.queues(sorted(queue_names))

        response = dict()
        response['broker_url'] = app.capp.connection().as_uri()
        response['queues'] = queues
        self.write(response)
