#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flower_ex.tasks import ListRegisteredTasks


ex_handles = [
    (r"/api/task/registered", ListRegisteredTasks),
]


