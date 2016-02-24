#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests import AsyncHTTPTestCase


class ListRegisteredTasksTest(AsyncHTTPTestCase):
    def test_task_page(self):
        r = self.get('/api/task/registered')
        self.assertEqual(200, r.code)
        self.assertTrue('task-registered' in str(r.body))


