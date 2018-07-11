#!/usr/bin/env python
import os
import sys
from unipath import Path
from django.core.files import uploadhandler

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bokwang.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# Mark : - Setting Payment PDF directory

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)
PROJECT_DIR = Path(__file__).ancestor(3)  # settings.py in settings dir
MEDIA_DIR = (PROJECT_DIR.child("Payment/OrderedRequestStorage"))
MEDIA_URL = "/Payment/OrderedRequestStorage"
