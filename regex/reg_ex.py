"""
Regular Expressions
"""

import re

def find_urls():
    URLS = """
    https://www.google.com
    http://coreyms.com
    https://youtube.com
    https://www.nasa.gov
    """

    pattern = re.compile(r'https?://(www.)?(\w+)(.\w+)')

    matches = pattern.finditer(URLS)

    for match in matches:
        print(match)

def find_emails():

    EMAILS = """
    CoreyMSchafer@gmail.com
    corey.schafer@university.edu
    corey-321-schafer@my-work.net
    """

    pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.\w+')

    matches = pattern.finditer(EMAILS)

    for match in matches:
        print(match)

def find_names():
    NAMES = """
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    """

    pattern = re.compile(r'(Mr|Ms|Mrs)\.? [A-Z]{1}\w*')

    matches = pattern.finditer(NAMES)

    for match in matches:
        print(match)
