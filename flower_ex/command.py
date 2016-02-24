#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TODO: File Comment
"""

from flower_ex.urls import extend_handles
from flower.command import FlowerCommand


class FlowerExCommand(FlowerCommand):
    """
    add register to Florist
    """
    def run_from_argv(self, prog_name, argv=None, **_kwargs):
        extend_handles()
        super(FlowerExCommand, self).run_from_argv(prog_name, argv=argv, **_kwargs)
