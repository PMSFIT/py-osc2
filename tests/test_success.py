import unittest

from .context import osc2parser, example_file

class TestCorrectParse(unittest.TestCase):

    def test_demo(self):
        self.assertEqual(osc2parser.parse_file(example_file('demo.osc'))[1],0)

    def test_swerving_side_vehicle(self):
        self.assertEqual(osc2parser.parse_file(example_file('swerving_side_vehicle.osc'))[1],0)

    def test_sample_expression(self):
        self.assertEqual(osc2parser.parse_file(example_file('sample_expression.osc'))[1],0)

    def test_namespaces(self):
        self.assertEqual(osc2parser.parse_file(example_file('namespaces.osc'))[1],0)

    def test_floatliterals(self):
        self.assertEqual(osc2parser.parse_file(example_file('float_literals.osc'))[1],0)

    def test_enums(self):
        self.assertEqual(osc2parser.parse_file(example_file('enums.osc'))[1],0)

if __name__ == '__main__':
    unittest.main()
