from .base import *


DEBUG = False

ADMINS = [("Jack", "contact@nicolaschartier.fr")]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
