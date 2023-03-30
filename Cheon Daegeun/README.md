## python Study django 3월 

###  2023년 3월 30일 python 스터디 공부 
| 날짜       | 제목               | 설명                                | 링크                                                                             |
| ---------- | ------------------ | ----------------------------------- | -------------------------------------------------------------------------------- |
| 2023 | django  | 1. 간단한 사이트 view 제작          |  |   |

### 2023년  간단한 사이트 view 제작 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accountapp.urls')),
]

_____________________________________

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Hello(request):
    return HttpResponse("Hello world!")

________________________________

from django.urls import path

from accountapp.views import Hello

app_name = "accountapp"



urlpatterns = [
    path('Hello/', Hello, name = 'Hello')
]

