#!/usr/bin/python3
"""Console test"""

import unittest
import console
from unittest.mock import patch
from io import StringIO

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
