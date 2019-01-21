import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 添加根目录apps在项目路径中
sys.path.insert(0,os.path.join(BASE_DIR,"apps"))

SECRET_KEY = 'b5@@yyioksi&c5y10=-r!+%ryp6gj=kf*q)!z%04iq=_0@qxxv'

DEBUG = True

ALLOWED_HOSTS = ["*"]

# 系统apps
SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 第三方apps
EXT_APPS = [
    "xadmin",
    "crispy_forms",
    "reversion"
]

# 项目apps
PROJECT_APPS = [
    "apps.home",
    "apps.detail",
    "apps.account",
    "apps.order",
    "apps.comment",
]

INSTALLED_APPS = SYSTEM_APPS +  EXT_APPS  +  PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OrangeMall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'OrangeMall.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "orange_mail",
        "HOST":"112.74.42.138",
        "USER":"root",
        "PASSWORD":"root",
        "PORT":3306,
    }
}



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



LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


######### 静态文件###############
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

############ 缓存配置(开发时先不要使用缓存)#################
CACHES = {
    "default": {
        # 使用redis做缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        # 缓存的地址
        'LOCATION': 'redis://112.74.42.138:6379/1',
        # rediss: //[:password]@localhost:6379 / 0
        'TIMEOUT': 2*60*60,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
    'session': {
        # 指定缓存的类型是文件缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        'LOCATION': 'redis://112.74.42.138:6379/15',
        'TIMEOUT': 300,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据(非必要)
            "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
}

# session使用redis座位缓存
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"


#########邮件验证设置 ############

EMAIL_HOST = 'smtp.163.com'

# 发送邮件接口
EMAIL_PORT = 25

# 发送邮件默认的名称
EMAIL_HOST_USER = 'chseng@163.com'

# 授权码
EMAIL_HOST_PASSWORD = 'qaz123456'

# 是否启用tls安全协议
EMAIL_USER_TLS = True















