#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tests import AsyncHTTPTestCase


class ListRegisteredTasksTest(AsyncHTTPTestCase):
    def test_task_page(self):
        r = self.get('/api/broker')
        self.assertEqual(200, r.code)
        self.assertTrue('broker_url' in str(r.body))
        self.assertTrue('queues' in str(r.body))

