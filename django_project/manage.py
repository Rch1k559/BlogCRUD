#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
This script serves as the entry point for managing the project. It can be used
to run development server, create database migrations, run tests, and more.
"""
import os
import sys


def main():
    """
    Run administrative tasks.
    This function sets up the environment by pointing to the project's settings file
    and then executes the command-line utility.
    """
    # Set the 'DJANGO_SETTINGS_MODULE' environment variable to our project's settings file.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        # Attempt to import the function that executes management commands.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django is not installed or not available, raise an informative error.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute the command passed from the command line.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # If the script is executed directly, call the main function.
    main()
