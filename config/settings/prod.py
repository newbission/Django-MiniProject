from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "storages",
]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
        "NAME": os.getenv("DB_NAME", "django"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': SECRET['DB']['NAME'],               # 데이터베이스 이름
#         'USER': SECRET['DB']['USER'],               # 사용자 이름
#         'PASSWORD': SECRET['DB']['PASSWORD'],       # 비밀번호
#         'HOST': SECRET['DB']['HOST'],               # 데이터베이스 서버 주소
#         'PORT': SECRET['DB']['PORT'],               # MySQL의 기본 포트
#     }
# }

# S3 Storage
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": os.getenv("S3_ACCESS_KEY", ""),
            "secret_key": os.getenv("S3_SECRET_ACCESS_KEY", ""),
            "bucket_name": os.getenv("S3_STORAGE_BUCKET_NAME", ""),
            "region_name": os.getenv("S3_REGION_NAME", ""),
            "location": "media",
            "default_acl": "public-read",
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": os.getenv("S3_ACCESS_KEY", ""),
            "secret_key": os.getenv("S3_SECRET_ACCESS_KEY", ""),
            "bucket_name": os.getenv("S3_STORAGE_BUCKET_NAME", ""),
            "region_name": os.getenv("S3_REGION_NAME", ""),
            "custom_domain": f'{os.getenv("S3_STORAGE_BUCKET_NAME", "")}.s3.amazonaws.com',
            "location": "static",
            "default_acl": "public-read",
        },
    },
}

# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#             "access_key": SECRET["S3"]["ACCESS"],
#             "secret_key": SECRET["S3"]["SECRET"],
#             "bucket_name": SECRET["S3"]["NAME"],
#             "region_name": SECRET["S3"]["REGION"],
#             "location": "media",
#             "default_acl": "public-read",
#         },
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#             "access_key": SECRET["S3"]["ACCESS"],
#             "secret_key": SECRET["S3"]["SECRET"],
#             "bucket_name": SECRET["S3"]["NAME"],
#             "region_name": SECRET["S3"]["REGION"],
#             "custom_domain": f'{SECRET["S3"]["NAME"]}.s3.amazonaws.com',
#             "location": "static",
#             "default_acl": "public-read",
#         },
#     },
# }

# Static, Media URL
STATIC_URL = f'https://{os.getenv("S3_STORAGE_BUCKET_NAME", "django-mini-project")}.s3.amazonaws.com/static/'
MEDIA_URL = f'https://{os.getenv("S3_STORAGE_BUCKET_NAME", "django-mini-project")}.s3.amazonaws.com/media/'
