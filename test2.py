import os
import unittest
import tempfile
import sys
from StringIO import StringIO
import urllib
from flask import Flask, Request, request
from flask.ext.testing import TestCase
from app import app

RESULT = False

class TestStringMethods(unittest.TestCase):

	def test_file_upload(self):

		class FileObj(StringIO):

			def close(self):
				global RESULT
				RESULT = True

		class MyRequest(Request):
			def _get_file_stream(*args, **kwargs):
				return FileObj()

		app = Flask(__name__)
		app.debug = True
		app.request_class = MyRequest

		@app.route("/import/", methods=['POST'])
		def upload():
			f = request.files['file']
			self.assertIsInstance(
			f.stream,
			FileObj,
			)
			# Note I've monkeypatched werkzeug.datastructures.FileStorage 
			# so it wont squash exceptions
			f.close()
			#f.stream.close()
			return 'ok'

		client = app.test_client()
		resp = client.post(
		'/import/',
		data = {
		'file': (StringIO('my file contents'), 'test_data.csv'),
		}
		)
		self.assertEqual(
		'ok',
		resp.data,
		)

if __name__ == '__main__':
    unittest.main()