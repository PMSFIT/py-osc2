import unittest

from .context import osc2parser, example_file

class TestErrorParse(unittest.TestCase):

    def test_demo_errors(self):
        self.assertEqual(osc2parser.parse_file(example_file('demo-error.osc'))[1],1)

if __name__ == '__main__':
    unittest.main()
