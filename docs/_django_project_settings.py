"""Django project settings for Sphinx documentation."""


from pathlib import Path

from environ.environ import Env


env = Env()
Env.read_env(env_file=Path(__file__).parent / '.env.template', overwrite=False)


# Quick-start development settings - unsuitable for production
# docs.djangoproject.com/en/dev/howto/deployment/checklist

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INTERNAL_IPS = ('127.0.0.1',)

ALLOWED_HOSTS = (
    '127.0.0.1', 'localhost',
    '.elasticbeanstalk.com',
)

# Application definition

INSTALLED_APPS = [
    # Django Admin Themes: add before django.contrib.admin
    # 'django_forest',
    'jazzmin',

    # Django Default/Main Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django Extensions: Extra Management Commands
    'django_extensions',

    # Query Profiling
    'silk',

    # REST Framework UI Templates
    'rest_framework',

    # CORS Headers
    'corsheaders',

    # Django Plotly Dash & related
    # TODO: 'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    'dpd_static_support',
    'whitenoise',

    # DjAI Data & Model modules
    'djai.data',
    'djai.model',
]

MIDDLEWARE = [
    # Kolo: add to top of MIDDLEWARE
    'kolo.middleware.KoloMiddleware',

    'django.middleware.security.SecurityMiddleware',

    # CORS: should be placed as high as possible,
    # especially before any middleware that can generate responses such as
    # Django's CommonMiddleware or Whitenoise's WhiteNoiseMiddleware
    'corsheaders.middleware.CorsMiddleware',

    # WhiteNoise: above all other middleware apart from SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Silk
    'silk.middleware.SilkyMiddleware',

    # Django Plotly Dash
    # - if the header and footer tags are in use:
    # TODO: 'django_plotly_dash.middleware.BaseMiddleware',
    # - if assets are being served locally through the use of
    # the global serve_locally or on a per-app basis:
    # TODO: 'django_plotly_dash.middleware.ExternalRedirectionMiddleware',
]

ROOT_URLCONF = 'urls'

# WSGI_APPLICATION = 'wsgi.application'

TEMPLATES = (
    dict(
        BACKEND='django.template.backends.django.DjangoTemplates',
        DIRS=(),
        APP_DIRS=True,
        OPTIONS=dict(
            context_processors=(
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            )
        )
    ),
)

# Database
# docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {'default': env.db()}

# docs.djangoproject.com/en/dev/ref/databases/#mysql-sql-mode
for db_config in DATABASES.values():
    if db_config['ENGINE'].endswith('mysql'):
        db_config['OPTIONS'] = \
            dict(init_command="SET sql_mode='STRICT_TRANS_TABLES'")

# Password validation
# docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = (
    dict(NAME=('django.contrib.auth.password_validation'
               '.UserAttributeSimilarityValidator')),
    dict(NAME=('django.contrib.auth.password_validation'
               '.MinimumLengthValidator')),
    dict(NAME=('django.contrib.auth.password_validation'
               '.CommonPasswordValidator')),
    dict(NAME=('django.contrib.auth.password_validation'
               '.NumericPasswordValidator')),
)

# Internationalization
# docs.djangoproject.com/en/dev/topics/i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# docs.djangoproject.com/en/dev/howto/static-files
STATIC_ROOT = '.staticfiles'
STATIC_URL = '/static/'   # must end with a slash

# Jazzmin Admin
JAZZMIN_SETTINGS = dict(
    # UI Customizer
    # Jazzmin has a built in UI configurator,
    # mimicked + enhanced from adminlte demo,
    # that allows you to customise parts of the interface interactively.
    # There will be an icon in the top right of the screen
    # that allows you to customise the interface.
    show_ui_builder=True,

    # title of the window
    site_title='DjAI Admin',

    # Title on the brand, and the login screen (19 chars max)
    site_header='DjAI Admin',

    # Welcome text on the login screen
    welcome_sign='Welcome to DjAI Admin',

    # Copyright on the footer
    copyright='DjAI'
)

# REST Framework
REST_FRAMEWORK = dict(
    DEFAULT_AUTHENTICATION_CLASSES=(
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),

    DEFAULT_PERMISSION_CLASSES=(
        'rest_framework.permissions.IsAuthenticated',
    ),

    DEFAULT_FILTER_BACKENDS=(
        'rest_framework.filters.OrderingFilter',
        'rest_framework_filters.backends.ComplexFilterBackend',
        'rest_framework_filters.backends.RestFrameworkFilterBackend',
    ),

    DEFAULT_PAGINATION_CLASS=('rest_framework.pagination.'
                              'LimitOffsetPagination'),
    PAGE_SIZE=25,

    DEFAULT_RENDERER_CLASSES=(
        # 'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.CoreJSONRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
)

# CORS Headers
CORS_ALLOW_ALL_ORIGINS = CORS_ORIGIN_ALLOW_ALL = True

# Uploads
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 ** 9   # ~1GB
FILE_UPLOAD_MAX_MEMORY_SIZE = 0   # save all uploaded files to disk

# Django Plotly Dash: frames within HTML documents
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Silky Query Profiling Settings
# SILKY_PYTHON_PROFILER = True
# SILKY_PYTHON_PROFILER_BINARY = True

SILKY_INTERCEPT_PERCENT = 100
SILKY_MAX_RECORDED_REQUESTS = 10 ** 3
SILKY_MAX_RECORDED_REQUESTS_CHECK_PERCENT = 100

SILKY_MAX_REQUEST_BODY_SIZE = -1   # Silk takes anything < 0 as no limit
SILKY_MAX_RESPONSE_BODY_SIZE = -1   # If response body > ? kb, ignore

SILKY_META = True

SILKY_STORAGE_CLASS = 'silk.storage.ProfilerResultStorage'
# SILKY_PYTHON_PROFILER_RESULT_PATH = '/path/to/profiles/'

SILKY_AUTHENTICATION = True   # User must login
SILKY_AUTHORISATION = True   # User must have permissions

SILKY_ANALYZE_QUERIES = True


# misc/other
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
