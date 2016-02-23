#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TODO: File Comment
"""


from __future__ import absolute_import
from __future__ import print_function

from flower_ex.command import FlowerExCommand
from flower.utils import bugreport


def main():
    try:
        flower_e = FlowerExCommand()
        flower_e.execute_from_commandline()
    except:
        import sys
        print(bugreport(app=flower_e.app), file=sys.stderr)
        raise


if __name__ == "__main__":
    main()
