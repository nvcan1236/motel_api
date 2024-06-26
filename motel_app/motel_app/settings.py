SITE_ID = 1
from pathlib import Path
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a^zb+yhpic9c7bxl4bn4iue=y$69+cy(a*f-)i#+np%zv8!k#='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'motel.apps.MotelConfig',
    'post.apps.PostConfig',
    # "authentication.apps.AuthenticationConfig",
    'ckeditor',
    'ckeditor_uploader',
    'oauth2_provider',
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    "rest_framework.authtoken",
    'django.contrib.sites',
    'django_filters',
    'vnpay',

    # google authentication config
    # 'auth_app',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware'

]
# STATIC_ROOT = "/home/CanhNguyen/motel_api/motel_app/static"
STATIC_ROOT = "static/"
MEDIA_ROOT = f'{BASE_DIR}/'
ROOT_URLCONF = 'motel_app.urls'
AUTH_USER_MODEL = 'motel.User'
CORS_ALLOW_ALL_ORIGINS = True
STATIC_URL = 'static/'
ALLOWED_HOSTS = ['*']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'motel_app.wsgi.application'
CKEDITOR_UPLOAD_PATH = "post/images/upload"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
import cloudinary

cloudinary.config(
    cloud_name='dbd7vfk12',
    api_key='381798527745373',
    api_secret='mq7kD-ynrQsabeC3zUXc5zHuDIY',
    # api_proxy="http://proxy.server:3128"
)

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moteldb',
        'USER': 'root',
        'PASSWORD': 'Myca@1236',
        'HOST': ''
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'motel$moteldb',
#         'USER': 'motel',
#         'PASSWORD': 'Myca@1236',
#         'HOST': 'motel.mysql.pythonanywhere-services.com'
#     }
# }
from dotenv import load_dotenv

load_dotenv()
SITE_ID = 2
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ["GOOGLE_CLIENT_ID"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

# Social app config
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'none'


# Email config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nvcan1236.test@gmail.com'
EMAIL_HOST_PASSWORD = 'yqgwpuwygngcnslw'
DEFAULT_FROM_EMAIL = 'nvcan1236.test@gmail.com'
DEFAULT_TO_EMAIL = 'nvcan1236.test@gmail.com'

# VNPAY Config
VNPAY_TMN_CODE = 'F6WDA8Q7'
VNPAY_HASH_SECRET_KEY = 'S53ZTBNG5TF5KCUFQ3SLPNUQE988JNKU'
VNPAY_PAYMENT_URL = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'
VNPAY_RETURN_URL = 'http://127.0.0.1:8000/vnpay/payment_return/'

# Thông tin app chúng thực bên Database online
# CLIENT_ID = 'O7s7zC71oV5apJerFffTTwqbiq9iC0sJ4obZknan'
# CLIENT_SECRET = 'WVPx5paiJ1vD0Fn8wBYUSKxWl6Jee9P6UYALwKZscgDPwURdBPbr8TjXWjWV7EJJTCvhh6npFZx1AfFNLkwjY9Ou6HaE0e1aRIfpHq6MtfyzkHby736WBzFavyv4hjb8'
#
# # Thông tin chứng thực local mysql
# # CLIENT_ID = 'SdDY7dKlhC0psQZvmKXDH14hXNSzqdVgc6cWF2Lg'
# # CLIENT_SECRET = 'P4cBbnWk6wiIvO5kaRjLKlqQyvHiJk5rfaBUT2z9Q3g9qxPNbyMxYT7ogg8GYpzf8k4ee22Fhw4e3i84b9wFZUWCfAkImKOAVpJNakrhQALhBOs45jwbkB0QPUWvgO7E'
#
# # Oauth app pythonanywhere
# # CLIENT_ID = '8OdjuOvhjzLFCigIbuw3mbDAlhWTirzeM7s1W1g2'
# # CLIENT_SECRET = '8pj5yZzwnH0vN3hflMrJJ7QBENDCsMKfIUlGQ15Gyg9GPTRCFXsIxm7iiF7xmcPf2IOz5uIXmfD9TjXJI3mKWHIQQ1HStaY3duHkIrSc4GWJGcyg1ZQgKtYIOxRksXia'
#
# Mật khẩu database online: Supabase@123