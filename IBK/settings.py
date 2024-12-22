from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-5w$flu!2smt1+9^^-1t9!t6m$!8*o!g+u46(9_+a8**7^_i9+*'
DEBUG = True
ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = 'home'  # 로그인 성공 후 이동할 페이지
LOGOUT_REDIRECT_URL = 'home'  # 로그아웃 후 이동할 페이지
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'IBK_ossproject',  # IBK 앱을 여기에 추가
    'crispy_forms',
    'crispy_bootstrap5',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IBK.urls'

# 템플릿 설정 추가
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 템플릿 루트 디렉토리
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
WSGI_APPLICATION = 'IBK.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # 전역 정적 파일 경로
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']  # CSRF 오류 해결

# 세션 설정-없어도 되긴함
SESSION_COOKIE_AGE = 3600  # 세션 유지 시간: 1시간 (초 단위)
SESSION_SAVE_EVERY_REQUEST = True  # 요청마다 세션 갱신


# 이메일 백엔드 설정 (로컬 개발에서 이메일을 실제로 보내지 않고 콘솔에 출력)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # 주석 처리하여 콘솔 출력을 비활성화

# 실제 이메일을 보내는 경우, Gmail SMTP 설정 예시
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# 본인 Gmail 계정과 앱 비밀번호 사용
EMAIL_HOST_USER = '20211896@edu.hanbat.ac.kr'  # 본인 Gmail 계정
EMAIL_HOST_PASSWORD = 'yanu lsie towe cxme'  # 앱 비밀번호 입력 (예: 'abcdefgh12345678')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
