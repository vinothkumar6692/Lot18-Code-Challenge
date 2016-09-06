import os
import unittest
import tempfile
import sys
import io
import urllib
from flask import Flask, Request, request
from flask import Flask
from flask.ext.testing import TestCase
from app import app

class StartingTestCase(TestCase):
	def setUp(self):
		self.client = app.test_client()

	def create_app(self):
		"""
		This is a requirement for Flask-Testing
		"""
		app = Flask(__name__)
		self.baseURL = "http://localhost:5000"
		return app

		# --------------------------------------------------------------------------
	    # Simple tests to make sure server is UP
	    # The Application MUST be running on the baseURL addr
	    # for this test to pass
	    # --------------------------------------------------------------------------

	def test_real_server_is_up_and_running(self):
		response = urllib.urlopen(self.baseURL)
		self.assertEqual(response.code, 200)
		# returned source code is stored in
		# response.read()

		# --------------------------------------------------------------------------
	    # Testing Views with GET
	    # --------------------------------------------------------------------------

	def test_view_form_get(self):
		resp = self.client.get('/')
		assert resp.status_code == 200
		assert 'Acme Wines' in str(resp.data)

	def test_get_orders(self):
		orders_url = self.baseURL+"/orders"
		response = urllib.urlopen(orders_url)
		assert response.code == 200

	def test_get_specific_order(self):
		orders_url = self.baseURL+"/orders/1111"
		response = urllib.urlopen(orders_url)
		assert response.code == 200

	def test_get_order_with_valid(self):
		orders_url = self.baseURL+"/orders?valid=1"
		response = urllib.urlopen(orders_url)
		assert response.code == 200

	def test_upload_with_dummy_data(self):
		post_data = {'text': 'wine service'}
		resp = self.client.post('/import/',
		data=post_data,
		follow_redirects=True)
		assert resp.status_code == 400

	

if __name__ == '__main__':
    unittest.main()