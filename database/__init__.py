import os


# check if django has been setup
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    from django import setup

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    setup()
    # Import models to make it available when importing the database package
    from .models import *
