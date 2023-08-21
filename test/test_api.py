import unittest

import webtest
from pyramid import testing
import hello_world


class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.app = webtest.TestApp(hello_world.app)

    def tearDown(self):
        testing.tearDown()

    def test_increment(self):
        resp0 = self.app.get('/')
        self.assertEqual(resp0.status_code, 200)

        resp1 = self.app.get('/')
        self.assertEqual(resp1.status_code, 200)

        self.assertEqual(
            resp0.json_body['count'] + 1,
            resp1.json_body['count'],
        )
