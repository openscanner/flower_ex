#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

from flower.api.tasks import BaseTaskHandler
from tornado import web


class ListRegisteredTasks(BaseTaskHandler):
    @web.authenticated
    def get(self):
        """
List (seen) task registered

**Example request**:

.. sourcecode:: http

  GET /api/task/registered HTTP/1.1
  Host: localhost:5555

**Example response**:

.. sourcecode:: http

  HTTP/1.1 200 OK
  Content-Length: 44
  Content-Type: application/json; charset=UTF-8

  {
      "task-registered": [
          "app.add"
      ]
  }

:reqheader Authorization: optional OAuth token to authenticate
:statuscode 200: no error
:statuscode 401: unauthorized request
        """
        capp_tasks = self.capp.tasks
        print(type(capp_tasks))
        tasks = list()
        for name in capp_tasks:
            # name = capp_task.name
            if not name.startswith('celery.'):
                tasks.append(name)

        response = dict()
        response['task-registered'] = tasks
        #response['task-registered'] = ["task.add", "tasks.sleep"]
        self.write(response)
