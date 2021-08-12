#!/usr/bin/python3
"""Console test"""

import unittest
import console
from unittest.mock import patch
from io import StringIO
import pep8

hbnb_console = console.HBNBCommand


class ConsoleTest(unittest.TestCase):
    """Unittest for console"""

    def CreateTest(self):
        """Create test"""
        with patch('sys.stdout', n=StringIO()) as file:
            hbnb_console().onecmd("create BaseModel")
            file.getvalue().strip()

        with patch('sys.stdout', n=StringIO()) as file:
            hbnb_console().onecmd("create BaseModel")
            file.getvalue().strip()

        with patch('sys.stdout', n=StringIO()) as file:
            hbnb_console().onecmd('create State name="California"')
            file.getvalue().strip()

    def test_pep8(self):
        """Check pep8 on console"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./console.py"])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py does not have documentation")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py does not have documentation")

    def test_prompt(self):
        """Test console prompt
        """
        self.assertEqual("(hbnb) ", hbnb_console.prompt)
