import os
from shutil import rmtree
from tempfile import mkdtemp
from unittest import TestCase

try:
    from io import StringIO         # Python 3
except:
    from StringIO import StringIO   # Python 2

class TestLecture(TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        rmtree(self.test_dir)

    def test_operation(self):
        from eric import operation
        self.assertEqual(operation(1, 1, '+'), 2)
        self.assertEqual(operation(1, 1, '*'), 1)
        self.assertEqual(operation(1, 1, '/'), 1)
        self.assertEqual(operation(1, 1, '-'), 0)
        self.assertRaises(TypeError, operation, 1, '1', '+')
        self.assertRaises(ValueError, operation, 1, 1, 'truc')

    def test_line_to_operation(self):
        from eric import line_to_operation

        for test_line in [
            '1;2;+\n',
            '1;2;+'
        ]:
            result = line_to_operation(test_line)
            self.assertTrue(isinstance(result, list))
            self.assertListEqual([1, 2, '+'], result)

    def test_saisie_int(self):
        from eric import saisie_int

        self.assertEqual(1, saisie_int('1'))
        self.assertRaises(ValueError, saisie_int, 'a')

    def test_saisie_ope(self):
        from eric import saisie_ope

        self.assertEqual('+', saisie_ope('+'))
        self.assertRaises(ValueError, saisie_ope, 'a')

    def test_ligne_output(self):
        from eric import ligne
        
        result = ligne('1;1;+')
        self.assertEqual(result, 2)
