#!/usr/bin/python3
"""Defines unittests for console.py."""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import console

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console_instance = console.HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        """Test quitting the program"""
        with self.assertRaises(SystemExit) as cm:
            self.console_instance.onecmd('quit')
        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_eof_handling(self, mock_stdout):
        """Test handling EOF (Ctrl+D)"""
        with self.assertRaises(SystemExit) as cm:
            self.console_instance.onecmd('EOF')
        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(mock_stdout.getvalue(), '\n')

    def test_custom_prompt(self):
        """Test that the custom prompt is correctly set"""
        self.assertEqual(self.console_instance.prompt, "(hbnb)")

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_line_handling(self, mock_stdout):
        """Test handling of an empty line"""
        self.console_instance.onecmd('')
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        """Test the "help" command"""
        self.console_instance.onecmd('help')
        self.assertIn("Documented commands (type help <topic>):", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_unknown_command_handling(self, mock_stdout):
        """Test handling of an unknown command"""
        self.console_instance.onecmd('unknown')
        self.assertIn("Unknown command: 'unknown'. Type 'help' for usage.", mock_stdout.getvalue())

class TestConsoleCreate(TestConsole):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_base_model(self, mock_stdout):
        """Test creating a new instance of BaseModel"""
        self.console_instance.onecmd('create BaseModel')
        self.assertIn('-', mock_stdout.getvalue())  # Replace with your expected output check
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class_name(self, mock_stdout):
        """Test creating with a missing class name"""
        self.console_instance.onecmd('create')
        self.assertIn("** class name missing **", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_nonexistent_class(self, mock_stdout):
        """Test creating with a nonexistent class name"""
        self.console_instance.onecmd('create NonExistentClass')
        self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
