#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flower.urls import handlers
from flower_ex.tasks import ListRegisteredTasks
from flower_ex.broker import BrokerInfo


_EXTENDED = False


def extend_handles():
    global _EXTENDED
    if not _EXTENDED:
        _EXTENDED = True
        ex_handles = [
            (r"/api/task/registered", ListRegisteredTasks),
            (r"/api/broker", BrokerInfo)
        ]

        # The last item in Flower URL's handles is ".*", so extended url should add to first
        for handle in ex_handles:
            handlers.insert(0, handle)

    return handlers


