2023년 3월 27일 파이썬 스터디 공부  
날짜	제목	설명	링크  
2023	파이썬 기초	함수 및 변수  	
print 출력  
예시 1)  
print("123")  
->123  
  
예시 2) number = 123  
print(num)  
->123  
  
함수 선언  
예시 1)  
def plus(a,b):  
return a+b  
print(plus(7,8))  
->15  
  
input 
예시 1) 
a = int(input("input num: ")) 
b = a * a 
print(b)  
    
if    
예시 1)   
a = int(input("input num: "))   
if a > 5:   
print(f'{a} is big number')   
elif a == 5:    
print(f'{a} is common number')    
else:   
print(f'{a} is small number')   
    
while 예시1)        
password=1432       
lock = True   
while lock:   
putnum = int(input("password : "))    
if password == putnum:    
print("OPEN")   
lock = False    
else:   
print("WORNG NUMBER")   
  
2023년 3월 28일 파이썬 스터디 공부  
날짜	제목	설명	링크  
2023	파이썬  

배열 선언 
number = [5,3,1,7,5,7,"asd",True,[134,12]]  
  
배열에 추가 하고싶을때  
number.append("asd) 
  
배열은 0부터 시작  

배열의 마지막 인덱스를 보고싶을 때 
number[-1]  
  
배열 선언 
  
player = {  
  "name" : nico,  
  "age" :21,  
  "alive" : True, 
} 

호출할때  
player[name]  
 	  
for loops 
    
websites=(  
"google.com", 
"airbnb.com", 
"twitter.com",  
"facebook.com", 
"tiktok.com"  
) 
  
for website in websites:  
print(website)  
  
  
  
websites = (  
"https://google.com", 
"airbnb.com", 
"https://twitter.com",  
"facebook.com", 
"https://tiktok.com"  
) 
  
for website in websites:  
if not websites.startswith("https://"): 
website = f"https://{websites}" 
  
2023년 4월 4일 파이썬 스터디 공부  
날짜	제목	설명	링크  
2023 장고스터디 view만들기

view.py 안에 함수 선언 해주기  
def hello_world(requset):  
    return HttpResponse('Hello world')    
  
메인 urls.py에 accountapp파일의 urls 인클루드 해주기  
from django.contrib import admin  
from django.urls import path, include  
  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('account/', include('accountapp.urls')),  
]    
  
accountapp 파일안에 urls.py 생성해주고  
   
from django.urls import path  
  
from accountapp.views import hello_world  
  
app_name = "accountapp"  
    
urlpatterns = [    
   path('hello_world/',hello_world,name = 'hello_world')  
    
터미널에 
python manage.py runserver 해주면 사이트에 Hello world 라고 뜨는것 확인가능  
  

    
    
  
