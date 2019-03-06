import unittest
from flask import current_app
from myflaskblog import create_app, db


class BasicTestCase(unittest.TestCase):
    def setup(self):
        self.app = current_app('testing_config')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exits(self):
        self.assertFalse(current_app is None)

