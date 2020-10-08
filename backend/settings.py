import os
from decouple import config
import django_heroku
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'core',
    'rest_framework',
    'django_celery_beat',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config()

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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

CELERY_BROKER_URL = config('REDIS_URL')
CELERY_RESULT_BACKEND = config('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

USERS_URLS = [
    "https://www.qwiklabs.com/public_profiles/72d824ca-9578-417b-b775-e4bc53b05544",
    "https://google.qwiklabs.com/public_profiles/fc640a10-1b08-476f-915b-da8f669a4389",
    "https://google.qwiklabs.com/public_profiles/7d9517c9-5bba-4ffb-b3a7-9bc3555700a5",
    "https://google.qwiklabs.com/public_profiles/2a42d1ca-73d8-44b9-a918-02baa581daf3",
    "https://google.qwiklabs.com/public_profiles/d8b9cd76-7697-4663-8c03-8232cc323dd6",
    "https://www.qwiklabs.com/public_profiles/7cae74c7-45ae-4b20-93b0-a2805acd0903",
    "https://www.qwiklabs.com/public_profiles/8c89c41d-01a7-4f67-93ae-3d31f3f0ac3d",
    "https://google.qwiklabs.com/public_profiles/cfdd31f8-3b15-4fa6-a6f1-93c1d1bc10c2",
    "https://www.qwiklabs.com/public_profiles/5e59a427-f054-4578-8a21-1e3bfef045c9",
    "https://google.qwiklabs.com/public_profiles/261c1fbf-d310-48db-b120-c030248f3d2d",
    "https://www.qwiklabs.com/public_profiles/e98ab6f7-52c0-4ea8-8b78-62827574bc3f",
    "https://google.qwiklabs.com/public_profiles/ef326837-1c57-498b-a784-1f1081deb826",
    "https://www.qwiklabs.com/public_profiles/0a5f9c38-b279-4d50-80c4-ae38606b7e88",
    "https://google.qwiklabs.com/public_profiles/75b858d7-e755-4ee3-afc4-a092d50dde90",
    "https://google.qwiklabs.com/public_profiles/c5d4e81d-12c3-41a9-8fcd-358c28c2d7cf",
    "https://www.qwiklabs.com/public_profiles/3b2dd7b9-fdb8-452f-b3a3-d021fb113c19",
    "https://google.qwiklabs.com/public_profiles/887b0d06-196a-4e97-afc7-c7cc62dda173",
    "https://google.qwiklabs.com/public_profiles/282fb6a6-4ab9-4639-9a3a-63fbe096fca6",
    "https://google.qwiklabs.com/public_profiles/277644f0-9c3f-4015-a37b-60d27fa39b33",
    "https://google.qwiklabs.com/public_profiles/40506142-81d0-4d46-af9b-4c812a24dcfa",
    "https://google.qwiklabs.com/public_profiles/0b7bfbca-5357-4dba-bd79-1e3474b5718b",
    "https://google.qwiklabs.com/public_profiles/0a434400-c893-4c8b-a190-a5217a6845f8",
    "https://www.qwiklabs.com/public_profiles/6770dc97-ed4e-467a-b52a-92b6b2e6c818",
    "https://google.qwiklabs.com/public_profiles/5922ce2d-3bda-47a4-9442-7491765548ed",
    "https://google.qwiklabs.com/public_profiles/4700e4db-ba37-4842-9df8-00f769ec6bec",
    "https://google.qwiklabs.com/public_profiles/47f5e401-6d0a-41a6-a4e6-06ef617620b3",
    "https://google.qwiklabs.com/public_profiles/cca77b2c-4221-4c50-b769-5b294b9c8d5a",
    "https://google.qwiklabs.com/public_profiles/38d25bc2-59a0-4855-a395-124c24be1975",
    "https://google.qwiklabs.com/public_profiles/ab2f0155-a185-46b6-9a33-bf7c2880bd85",
    "https://google.qwiklabs.com/public_profiles/a709d17e-f9b4-4644-a8c7-c49fa79e093e",
    "https://www.qwiklabs.com/public_profiles/2d28e440-b91f-43ef-9e58-ccbf516b2e58",
    "https://www.qwiklabs.com/public_profiles/4af8beba-74f0-4c8a-ad84-5d1672e226bc",
    "https://www.qwiklabs.com/public_profiles/99d6076c-ccd3-4022-b43d-267aa65f453f",
    "https://www.qwiklabs.com/public_profiles/d0ba12fb-0ff7-4a5f-a53b-3d0adc5a77fc",
    "https://google.qwiklabs.com/public_profiles/4522cbc0-3594-4872-aebf-ac2dcd151809",
    "https://google.qwiklabs.com/public_profiles/bc71fd85-5aa5-483d-af03-ba8166606de3",
    "https://www.qwiklabs.com/public_profiles/31d4af83-0069-408b-8bab-71971ff16aab",
    "https://google.qwiklabs.com/public_profiles/ec6e6dc9-22ad-4a1b-a5fa-d1d0b41275c9",
    "https://www.qwiklabs.com/public_profiles/f1288ec9-b42f-41b8-a972-97c58d03b848",
    "https://google.qwiklabs.com/public_profiles/a6d32e71-975c-48c5-bc4f-cd23c093dff3",
    "https://www.qwiklabs.com/public_profiles/33e4dc89-d676-4ae6-bc5b-2f7a5fdb9c79",
    "https://google.qwiklabs.com/public_profiles/4627259f-54fa-4dcc-a3d4-359a780d7cc8",
    "https://www.qwiklabs.com/public_profiles/e8be337b-f1bb-4ce9-8255-c184826bd9e5",
    "https://google.qwiklabs.com/public_profiles/308fe491-5488-4730-97e0-8b448905e748",
    "https://google.qwiklabs.com/public_profiles/6eb92109-538c-4827-b6e0-bcb198c7e6eb",
    "https://www.qwiklabs.com/public_profiles/e3b149a7-6ba9-4039-8951-2b1171a5fa3e",
    "https://google.qwiklabs.com/public_profiles/03d6690a-2e0d-4fe8-b900-2c03c566eb4a",
    "https://google.qwiklabs.com/public_profiles/b2c1cb57-e249-49f5-8aaf-ae0b07c12892",
    "https://www.qwiklabs.com/public_profiles/3db11df6-4b95-4c01-b2c8-78c24ba0f955",
    "https://www.qwiklabs.com/public_profiles/7b67eeb2-27c2-4160-a722-fc3d6ad6a9ed",
    "https://www.qwiklabs.com/public_profiles/1ef36f70-c7a0-43ad-a910-4ca8632a0ca9",
    "https://www.qwiklabs.com/public_profiles/7e88c24e-d179-4d57-88b6-43d1e0a9bc72",
    "https://www.qwiklabs.com/public_profiles/b8f34258-7114-4f14-a8af-ca7f87460d3a",
    "https://www.qwiklabs.com/public_profiles/a4fb83cc-955a-420b-8d28-f4b195e0a0fe",
    "https://www.qwiklabs.com/public_profiles/16e3a02c-f0b6-4cd2-9634-327602d7e1c9",
    "https://google.qwiklabs.com/public_profiles/cb83d57b-9796-43b7-915e-ff2e92a0b152",
    "https://google.qwiklabs.com/public_profiles/1a62cec7-b21d-434e-8752-8875487ca0d6",
    "https://google.qwiklabs.com/public_profiles/a4f6be66-8dba-4da8-ba47-8e0a3ba7fc4e",
    "https://www.qwiklabs.com/public_profiles/cd342976-35b1-48ce-825a-f2d8865c96ad",
    "https://google.qwiklabs.com/public_profiles/cd8afd56-767c-4de7-b25e-7cba5bc653cc",
    "https://google.qwiklabs.com/public_profiles/a78cd1e0-4683-467a-bfbf-31e8a5999247",
    "https://google.qwiklabs.com/public_profiles/e39ecc52-a7aa-49a0-832f-13970d246f01",
    "https://www.qwiklabs.com/public_profiles/9719659f-e91d-41f9-8e21-36eb5b20cc9b",
    "https://www.qwiklabs.com/public_profiles/430d6aa6-8986-46bd-9f3e-3f8251b00ed8",
    "https://google.qwiklabs.com/public_profiles/6dec274d-f7fd-44e2-88d2-f130b4a75d02",
    "https://google.qwiklabs.com/public_profiles/2dc1f27f-74c0-402d-8834-c24e133d8808",
    "https://www.qwiklabs.com/public_profiles/c16a628e-fe1a-4186-aaa5-40d81699e042",
    "https://www.qwiklabs.com/public_profiles/b18e7b43-c2d6-48aa-9d3d-edd172df18d5",
    "https://google.qwiklabs.com/public_profiles/4d056da7-91d0-4e2a-a13c-f974155d8faf",
    "https://www.qwiklabs.com/public_profiles/62b2168d-62dc-4794-9845-37ab6d456ca0",
    "https://google.qwiklabs.com/public_profiles/cd8bfda6-1517-48e8-b4a2-804301a7076e",
    "https://google.qwiklabs.com/public_profiles/a1e61909-f193-4dd2-a1de-6e35c587d49d",
    "https://www.qwiklabs.com/public_profiles/e84cb1ba-8710-4d01-a6ba-d62c23462bd8",
    "https://google.qwiklabs.com/public_profiles/f6f32c1e-e720-4837-b006-5800bc9ff635",
    "https://google.qwiklabs.com/public_profiles/753c30d0-5a24-4c57-8056-eddfcf18b9b9",
    "https://google.qwiklabs.com/public_profiles/f1aacc3a-1a5a-4fea-a37d-7df7f41d7d7f",
    "https://google.qwiklabs.com/public_profiles/eb4c54b4-91f8-4448-b918-aa08b1b3957e",
    "https://google.qwiklabs.com/public_profiles/6b34398c-dff3-4b1c-9323-a55c3fbcd709",
    "https://www.qwiklabs.com/public_profiles/f57da176-a262-4b24-89f4-600e5b4797be",
    "https://www.qwiklabs.com/public_profiles/d9ff896c-196b-47de-8ee0-b68538494a23",
    "https://google.qwiklabs.com/public_profiles/b3ced915-28b4-4d74-8084-e1d98ec1e476",
    "https://www.qwiklabs.com/public_profiles/c4e43646-c985-45cf-90c3-693914fc792a",
    "https://www.qwiklabs.com/public_profiles/e540f851-56a9-4557-9939-a84bba9bbbcc",
    "https://www.qwiklabs.com/public_profiles/936c8e4a-eb94-4a59-a86f-6d3ea3b30631",
    "https://www.qwiklabs.com/public_profiles/72bc76bd-b3e7-451e-84fc-010267200aae",
    "https://www.qwiklabs.com/public_profiles/9b9d4d18-e78b-461e-a808-95eb4170764a",
    "https://google.qwiklabs.com/public_profiles/76e2dbb5-da84-47af-8243-f73e0a3376e0",
    "https://google.qwiklabs.com/public_profiles/77f20236-9c45-4683-b357-abcbf78adcb5",
    "https://www.qwiklabs.com/public_profiles/5e24dab3-2980-45c9-9c3f-a82a650c4b8b",
    "https://www.qwiklabs.com/public_profiles/01e4097c-9daf-4e8f-b629-ad70f0a6f96e",
    "https://www.qwiklabs.com/public_profiles/0a17545a-a362-43a7-836c-4d7be71a2cb1",
]


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Cache-Control',
    'X-Requested-With',
]


CELERY_BEAT_SCHEDULE = {
    'generate-report': {
       'task': 'core.tasks.summary',
       'schedule': 1200.0,
    },

}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}


django_heroku.settings(locals())
