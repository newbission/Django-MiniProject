from .base import *

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = "config.dev_urls"

INSTALLED_APPS += [
    "drf_yasg",
]

# Static
STATIC_URL = "static/"
STATIC_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / ".static_root"

# Media
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgressql",
        "HOST": os.getenv("DB_PORT", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
        "NAME": os.getenv("DB_NAME", "django"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
    }
}
CELERY_BEAT_SCHEDULE = {
    # 작업 스케줄
    "weekly-analyze-and-notify": {
        "task": "analysis.tasks.weekly_analyze_and_notify_user",
        "schedule": crontab(),
    },
    "monthly-analyze-and-notify": {
        "task": "analysis.tasks.monthly_analyze_and_notify_user",
        "schedule": crontab(),
    },
}
