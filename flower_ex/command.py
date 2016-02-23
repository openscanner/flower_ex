#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TODO: File Comment
"""

from flower_ex.urls import ex_handles
from flower.urls import handlers
from flower.command import FlowerCommand


class FlowerExCommand(FlowerCommand):
    """
    add register to Florist
    """
    def run_from_argv(self, prog_name, argv=None, **_kwargs):
        # The last item in Flower URL's handles is ".*", so extended url should add to first
        # handlers.extend(ex_handles)
        for handle in ex_handles:
            handlers.insert(0, handle)
        # print(handlers)

        super(FlowerExCommand, self).run_from_argv(prog_name, argv=argv, **_kwargs)
