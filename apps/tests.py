import os

from django.test import TestCase

# Create your tests here.
print(f"SECRET_KEY: {os.getenv('SECRET_KEY')}")
