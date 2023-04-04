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

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

env = 부분에서 오류 발생

> 	.env
DEBUG=on
SECRET_KEY=django-insecure-#4_tm5hn+wqtb&!xpmt)#r)m5&i@2v-iz76$u6+e#$wg2irzcn
DATABASE_URL=psql://urser:un-githubbedpasswod@127.0.0.1:8458/database
SQLITE_URL=sqlite:///my-local-sqlite.db
CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213
REDIS_URL=rediscache://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret

2023 03 31 스터디

<!DOCTYPE html>
<html lang="ko">

{% include 'head.html' %}

<body>
    {% include 'header.html' %}

    <hr>

    {% block content %}
    {% endblock %}

    <hr>

    {% include 'footer.html' %}
</body>
</html>

head 파일에서 style 수정, 글꼴을 바꿈

- footer.html
<div style="text-align:center; margin-top: 2rem;">

        <div style="font-size: .6rem;">
            <span>공지사항</span> |
            <span>제휴문의</span> |
            <span>서비스 소개</span>
        </div>
        <div style="margin-top: 1rem;">
            <h6 style="margin-top: 1rem; font-family: 'PT Serif', serif;">Pragmatic</h6>
        </div>

    </div>

-header.html
<div style="text-align:center; margin: 2rem 0;">
        <div>
            <h1 style="font-family: 'PT Serif', serif;">Pragmatic</h1>
        </div>
        <div>
            <span>nav1</span>
            <span>nav2</span>
            <span>nav3</span>
            <span>nav4</span>
        </div>

    </div>


    - base.css 파일 만들기

    .pragmatic_logo {
    font-family: 'PT Serif', serif;
}

.pragmatic_footer_button {
     font-size: .6rem;
}

.pragmatic_footer {
     text-align:center; margin-top: 2rem;
}

.pragmatic_header {
    text-align:center;
    margin: 2rem 0;
}

- footer와 header에 있는 css 내용을 base.css 파일을 만들어 따로 작성하였다
- px,em,rem,%
- 1rem = 16px

-- 23-04-02 스터디

<div style="height: 20rem; background-color: #38df81; border-radius: 1rem; margin: 2rem;">
        <h1>
          testing
        </h1>

        <form action="/account/hello_world/" method="post">
            {% csrf_token %}
            <input type="submit" class="btn btn-primary" value="POST">
        </form>

        <h1>
            {{ text }}
        </h1>


def hello_world(request):

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!!!!!!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!!!!!'})

{% csrf_token %}
= 장고에서 제공하는 보안 기능들 중 하나


--- 23-04-03 스터디

- hello_world.html

<div style="border-radius: 1rem; margin: 2rem; text-align: center">
        <h1 style="font-family: 'PT Serif, cursive;">
            Hello World LIST!!
        </h1>
        <h1>
          testing
        </h1>

        <form action="/account/hello_world/" method="post">
            {% csrf_token %}
            <div>
                <input type="text" name="hello_world_input">
            </div>
            <div>
                <input type="submit" class="btn btn-primary" value="POST">
            </div>
        </form>

        {% if hello_world_list %}
            {% for hello_world in hello_world_list %}
            <h4>
                {{ hello_world.text }}
            </h4>
            {% endfor %}
        {% endif %}

    </div>

- views.py

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})



