from pathlib import Path
from decouple import config

INSTALLED_APPS = [
    "database",
]
SECRET_KEY = "-lvtr7r+tthuuzadww=ppmp8#xkhs8eh_jya844ynh_^h@)m#d"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

BASE_DIR = Path(__file__).resolve().parent.parent

MODE = config("MODE", default="dev")

if MODE == "dev":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "PORT": config("DB_PORT"),
        }
    }
