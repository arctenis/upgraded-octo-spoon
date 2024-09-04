from .base import *
import os


DEBUG = False

# ADMINS = [("Jack", "jack@example.com")]

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SECRET_KEY = os.environ.get("SECRET_KEY")

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True
