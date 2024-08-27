# Django Configuration

## new django app

- 在目标文件夹下,安装虚拟环境: pipenv install django
- 新建 django 项目: django-admin startproject admin .
- 新建 app: ./manage.py startapp ipredict
- 查看虚拟环境位置: pipenv --venv

## other dependencies

- 安装 Debug-toolbar

  - python -m pip install django-debug-toolbar
  - INSTALLED_APPS: 'debug_toolbar', 应该在 django.contrib.staticfiles 之后
  - MIDDLEWARE: 'debug_toolbar.middleware.DebugToolbarMiddleware'
  - INTERNAL_IPS: '127.0.0.1'
  - urlpatterns: path('**debug**/', include(debug_toolbar.urls))

- 安装 Django REST Framework

  - pipenv install djangorestframework
  - Installed app: 'rest_framework',

- 显示的小数不要 string

```Python
REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False
}
```

- 安装 Nested Routers

  - pipenv install drf-nested-routers
  - from rest_framework_nested import routers

- 安装 django-filter,为了使 url 可以使用查询,部分返回. 具体查看 doc：google django filters
  - Pipenv install django-filter
  - Installed app: 'django_filters',
  - from django_filters.rest_framework import DjangoFilterBackend

## Authenticate

- authentication

  - AUTH_USER_MODEL = 'core.User'

- Djoser

  - pipenv install djoser
  - Installed app: 'djoser',
  - 总 url 处,添加 path('auth/', include('djoser.urls')),

- djoser 只是一个 api layer,我们依然需要一个 authentic engine or backend to do the actual work
- 有两个选择,一可以用 token based authentication built in django rest framework.方法一需要在数据库存储使用单独的 table 存储 token,所以每一次 request,都需要去后端访问一次数据库,来验证这个 token 是否有效。
- 二是 JSON web token authentication implemented in a separate library。方法二,每个 token 都有一个 digital,on the server we can use the signature to ensure this is a valid token
- 以下是方法二需要的 dependency：
  - pipenv install djangorestframework_simplejwt

```Python
REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
	'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
}

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]
```

- 以下在 settings 中,因为想 register 的时候,看到 custom 的 field(first name last name),需要告诉 djoser,特别使用的 serilizers(custom 的 serializer 在 core 中)

```Python
DJOSER = {
    'SERIALIZERS': {
        'user_create': 'core.serializers.UserCreateSerializer',
        'current_user': 'core.serializers.UserSerializer'
    }
}

Settings.py:
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}
```

## mieda folder and background task

- 添加 media folder

```Python
Import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- Develop mode urls.py

```Python
from django.conf.urls.static import static
from django.conf import settings

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- 因为要使用 models.ImageField,需要安装 pillow

  - pipenv install pillow

- 安装 django-cors-headers,装这个是为了 client app hosted on another domain 可以访问 backend server
- Cors(cross-origin-resource-sharing), this policy prevents an app hosted on one domain form sending a request to an app hosted on another domain  
  这个中间件应该尽量往前放
  - pipenv install django-cors-headers

```Python
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'django_filters',
    'corsheaders',
    'rest_framework',
    'djoser',
    'playground',
    'debug_toolbar',
]
'corsheaders',
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
'corsheaders.middleware.CorsMiddleware',
```

```Python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8001',
    'http://127.0.0.1:8001',
]
```

- D for detach, p for specify a port mapping

```Docker
docker run -d -p 6379:6379 redis
docker ps	# List the running container
Pipenv install redis
Pipenv install flower
```

- 为了使用 SQL engine，安装 mssql-django
  - pipenv install mssql-django

# Quick Recite

- 下载 database 中的 model: python manage.py inspectdb --database=us_db > legency.py
- To reverse all migrations for an app: ./manage.py migrate my_app zero
- djoser re-set password: /auth/users/set_password/
- python manage.py changepassword <user_name>
- relation
  - book = Book.objects.select_related('author').get(id=1)
  - book = Book.objects.prefetch_related('tags').get(id=1)
  - prefetch_related: Product.objects.prefetch_related('images').all()
  - prefetch_related: Cart.objects.prefetch_related('items\_\_product').all()
  - select_related: CartItem.objects.filter(cart_id=self.kwargs['cart_pk']).select_related('product'), 一个 cart item 只有一个 prdocut 与之对应，多对一
- pip freeze > requirements.txt
- pipenv requirements > requirements.txt
- pip3 freeze -l > requirements.txt
- 特定 app make migations: python manage.py makemigrations us_branch
- 特定 app & database, 进行 migrate: ./manage.py migrate us_branch --database=us_db
