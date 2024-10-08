import unittest
from app import create_app, db
from app.models import Property

class PropertyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_list_property(self):
        # Implement test for listing property
        pass

    def test_purchase_property(self):
        # Implement test for purchasing property
        pass