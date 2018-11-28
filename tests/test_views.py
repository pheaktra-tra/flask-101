# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_products_return_no_item(self):
        response = self.client.get("/api/v1/products/5")
        products = response.json
        self.assertEquals(response.status_code, 404)

    def test_products_return_1_item(self):
        response = self.client.get("/api/v1/products/3")
        products = response.json
        self.assertEquals(response.status_code, 200)

    def test_products_return_1_item_name(self):
        # import pdb; pdb.set_trace()
        response = self.client.get("/api/v1/products/3")
        products = response.json
        self.assertEquals(response.json.get('name'), 'test')


    def test_delete_a_product(self):
        response = self.client.delete("/api/v1/products/3")
        products = response.json
        self.assertEquals(response.status_code, 204)

