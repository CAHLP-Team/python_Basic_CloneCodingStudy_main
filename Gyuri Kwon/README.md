## Python Study TIL 3월 

###  2023년 3월 30일 파이썬 스터디 공부 
| 날짜       | 제목               | 설명                                | 링크                                                                             |
| ---------- | ------------------ | ----------------------------------- | -------------------------------------------------------------------------------- |
| 2023 | django 기초  | 1. git 공부          |  |   |

### 2023년  git 기초 

* Pycharm에서 출력하는 방법 
> 	settings.py
from pathlib import Path

import os, environ
env = environ.Evn(
    #set casting, default value
    DEBUG=(bool, False)
)


#Build paths inside the project like this: BASE_DIR / 'subider'.
BASE_DIR = Path(__file__).resolve().parent.parent

#reading .env file
environ.Env.read_env(
    env.file= os.path.join(BASE_DIR, '.env')
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

env = 부분에서 오류 발생

> 	.env
DEBUG=on
SECRET_KEY=django-insecure-#4_tm5hn+wqtb&!xpmt)#r)m5&i@2v-iz76$u6+e#$wg2irzcn
DATABASE_URL=psql://urser:un-githubbedpasswod@127.0.0.1:8458/database
SQLITE_URL=sqlite:///my-local-sqlite.db
CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213
REDIS_URL=rediscache://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret


