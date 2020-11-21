import sys
import unittest
from importlib import import_module


class FlaskTestCase(unittest.TestCase):
    def test_get_ok(self):
        sys.path.append('..')
        flask_app = import_module('main1')
        flask_app.app.testing = True
        with flask_app.app.test_client() as c:
            result = c.get('/result?fruit_no=1')
            assert 'もも' in result.get_data(as_text=True)

    def test_get_ng(self):
        sys.path.append('..')
        flask_app = import_module('main1')
        flask_app.app.testing = True
        # with self.assertRaises(KeyError):
        with flask_app.app.test_client() as c:
            with self.assertRaises(KeyError) as e:
                result = c.get('/result?fruit_no=5')

            self.assertEqual(e.exception.args[0], '5')
