## Python Study TIL 2월
중요, 확인
>참고 링크:https://nomadcoders.co/python-for-beginners/lobby

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 17일 파이썬 스터디 공부
>print(), 변수, 데이터 타입, 함수, 문법, 매개변수

## print()
~~~
print(변수)
 # print가 끝나면 줄을 바꿈

print("hello")
~~~
>결과<br>hello
## 변수

>***숫자를 저장하기 위한 변수***
~~~
myage = 99   #상관 없지만 보기 안 좋음
myAge = 99   #camel case 자바스크립트에서 사용됨
my_age = 99  #snake case 파이썬에서 사용됨
             #둘 다 써도 상관 없음
my age = 99  #공백X
1my_age = 00 #숫자가 앞에 와도 안 됨, 특수문자도X
~~~

>***문자를 저장하기 위한 변수***
<br>글자로 취급하기 따옴표가 있어야 됨
~~~
my_name = "User012050"
my_age = "99"
~~~

>***참 거짓을 나타내는 변수***
<br>Booleans
~~~
my_name = True
my_age = False
~~~

## 함수

***함수 정의***
~~~
 #변수랑 똑같이 숫자로 시작하면 안 됨
def say_hello():
  print("hello how r u?")
~~~

***함수 호출***
~~~
say_hello()
~~~

***함수의 역할*** - 여러가지 기능을 가진 문장을 하나로 합친다.
~~~
def say_hello():
  print("hello how r u?")
  print("hello how r u?")
  print("hello how r u?")

say_hello()
~~~

~~~
print("hello how r u?")
print("hello how r u?")
print("hello how r u?")
~~~

## 문법

~~~
def say_hello():
print("hello how r u?") #에러
~~~
>파이썬은 들여쓰기를 통해서 중괄호 역할을 대신한다

~~~
def say_hello():
  print("hello how r u?")
~~~
>tab을 통해서 들여쓰기를 할 수 있다.

## 매개변수
함수가 받을 데이터를 나타냄
~~~
def say_hello(user_name):
  print("hello", user_name,"how r u?")

say_hello("User012050")
say_hello("lynn")
~~~
>결과<br>hello User012050 how r u?<br>hello lynn how r u?

~~~
def say_hello(user_name, user_age):
  print("hello", user_name,"how r u?")
  print("you are", user_age, "years old")

say_hello("User012050", 99)
~~~

>결과<br>hello User012050 how r u?<br>you are 99 years old


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 18일 파이썬 스터디 공부
>함수 기본값, return, if, else, elif

## 함수 기본값
~~~
def say_hello(user_name = "User012050", user_age = 99):
  print("hello", user_name,"how are you?")
  print("you are", user_age, "years old")

say_hello()
say_hello("User050210", 101)
~~~
>결과<br>hello User012050 how are you?<br>you are 99 years old<br>hello User050210 how are you?<br>you are 101 years old

***확인***<br>
하나는 default 값을 쓰고 다른 하나는 값을 넣고 싶을 때 하는 방법 찾아보기<br>
>->기본 매개변수를 사용할 때 한가지 지켜야 할 점은, 기본 매개변수를 non-default value parameter의 앞에 배치해야 한다는 점이다.<br>
출처:https://url.kr/whzlb8
<br><h6>또는</h6>say_hello(user_age = 101)이렇게 할 수도 있다.

## return

~~~
def tax_cal(money):
  return money * 0.35

def pay_tax(tax):
  print("Thank you for paying", tax)

to_pay = tax_cal(100)
pay_tax(to_pay)
~~~

같은 결과를 보여줌
~~~
def tax_cal(money):
  return money * 0.35

def pay_tax(tax):
  print("Thank you for paying", tax)

pay_tax(tax_cal(100))
~~~

>결과<br>Thank you for paying 35.0

***중요***<br>
,(쉼표)를 쓰지 않고 문장에 변수를 넣는 방법
~~~
def hello(word):
  print(f"hello {word}")
  
hello("User012050")
~~~

>결과<br>hello User012050

## if, else, elif

if
~~~
if True:
  print("it is True1")

a = "abc"
if a == "abc":
  print("it is True2")

a = 123
if a > 10:
  print("it is True3")
~~~

>if 뒤의 결과가 true이면 if 안의 문장을 실행한다.

<br>
else

~~~
if False:
  print("it is True1")
else:
  print("it is False")
~~~

>if의 조건이 false일 때, else 안의 문장을 실행한다.

<br>

elif
~~~
winner = 10
if winner > 10:
  print("winner is greater than 10")
elif winner == 10:
  print("winner is 10")
else:
  print("winner is less than 10")
~~~

>결과<br>winner is 10

>if가 거짓이고 elif의 조건이 참일 때 elif 안의 문장이 실행된다.

if > elif > else 순으로 동작한다.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 19일 파이썬 스터디 공부
>input, type, int, and, or, Standard Library, while

## input

하나의 argument만 받고 그 값을 return함<br>사용자에게 질물은 하는 함수
~~~
age = input("How old are you?")
print("user answer", age)
~~~

## type 

~~~
age = input("How old are you?")
print(type(age))
~~~

>How old are you?123<br><class 'str'>

숫자로 값을 받고 싶을 때는 int를 사용

~~~
age = int(input("How old are you?"))
print(type(age))
~~~

>How old are you?123<br><class 'int'>

## and

양쪽의 값이 다 참이여야 된다.

~~~
age = int(input("How old are you?"))
if age < 18:
  print("You can't drink.")
elif age >= 18 and age <= 35:
  print("You drink beer!")
else:
  print("Go ahead!")
~~~

## or

둘 중에서 하나라도 참이면 된다.

~~~
age = int(input("How old are you?"))
if age < 18:
  print("You can't drink.")
elif age >= 18 and age <= 35:
  print("You drink beer!")
elif age == 60 or age == 70:
  print("Birthday party!")
else:
  print("Go ahead!")
~~~

정리

~~~
True and  True == True
False and True == False
True and False == False
False and False == False

True or True == True
True or False == True
False or True == True
False or False == False
~~~

## Standard Library

>이미 언어에 포함된 function들의 그룹

https://docs.python.org/ko/3.12/library/

## while

조건이 참일 때 while 안의 문장을 무한 반복함

~~~
distance = 0
while distance < 20:
  print("I'm running:", distance,"km")
  distance = distance + 1
~~~

>결과<br>I'm running: 0 km<br>I'm running: 1 km<br>I'm running: 2 km<br>I'm running: 3 km<br>I'm running: 4 km<br>I'm running: 5 km<br>I'm running: 6 km<br>I'm running: 7 km<br>I'm running: 8 km<br>I'm running: 9 km<br>I'm running: 10 km<br>I'm running: 11 km<br>I'm running: 12 km<br>I'm running: 13 km<br>I'm running: 14 km<br>I'm running: 15 km<br>I'm running: 16 km<br>I'm running: 17 km<br>I'm running: 18 km<br>I'm running: 19 km


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 20일 파이썬 스터디 공부
>list, str methods, tuple, dictionary

## list

~~~
days_of_week = ["mon", "Tue", "Wed", "Thur", "Fri"]
print(days_of_week)
~~~

>['mon', 'Tue', 'Wed', 'Thur', 'Fri']

특정 리스트 선택

~~~
days_of_week = ["mon", "Tue", "Wed", "Thur", "Fri"]
print(days_of_week[3])
~~~

~~~
days_of_week = [1, 2, 3, True, False, "hi", "black", [ 1, 2, 3, [False, True]]]
print(days_of_week[7][3][1])
~~~

>True


## method

https://docs.python.org/ko/3.12/library/stdtypes.html#text-sequence-type-str

***.upper()***
<br>
데이터를 대문자로 바꿔준다

~~~
name = "abc"
print(name.upper())
~~~

>ABC



***.capitalize()***
<br>첫 번째 글자를 대문자로 바꿔줌<br>

***확인***
string인 name variable 안에는 capitalize라는 method가 있다.

~~~
name ="nico"
print(name.capitalize())
~~~

>Nico

***.startswith("문자")***
<br>첫 번째 글자가 따옴표 안의 글자인이 아닌지 확인해 줌

~~~
name = "nico"
print(name.startswith("n"))
~~~

***.replace("문자", "문자")***

<br>해당 문자를 다른 문자로 대체함

~~~
name = "nico"
print(name.replace("o", "><"))
~~~

>nic><

***.endswith("문자")***

~~~
name = "nico"
print(name.endswith("f"))
~~~

>False

## 다른 형태

~~~
print("nico".endswith("f"))
~~~

## 더 많은 메소드

+ clear()
+ reverse()
+ append("data")

## tuple

~~~
days = ("Mon", "Tue", "Wed")
days.append("Fri")
~~~

>에러

튜플은 수정할 수 없다.


## dictionary

***속성을 가지고 있는 데이터를 만들 때 쓰임***

~~~
player = {
  'name' : 'nico', 
  'age' : 12,
  'alive' : True
}
print(player)
~~~

>{'name': 'nico', 'age': 12, 'alive': True}

~~~
player = {
  'name' : 'nico', 
  'age' : 12,
  'alive' : True,
  'fav_food' : ["pizza", "burger"]
}
print(player.get('age'))
print(player['fav_food'])
~~~

>12<br>['pizza', 'burger']

데이터 삭제

~~~
player = {
  'name' : 'nico', 
  'age' : 12,
  'alive' : True,
  'fav_food' : ["pizza", "burger"]
}
player.pop('age')
print(player)
~~~

>{'name': 'nico', 'alive': True, 'fav_food': ['pizza', 'burger']}

데이터 추가

~~~
player = {
  'name' : 'nico', 
  'age' : 12,
  'alive' : True,
  'fav_food' : ["pizza", "burger"]
}
player['xp'] = 1500
print(player)
~~~

>{'name': 'nico', 'age': 12, 'alive': True, 'fav_food': ['pizza', 'burger'], 'xp': 1500}

~~~
player = {
  'name' : 'nico', 
  'age' : 12,
  'alive' : True,
  'fav_food' : ["pizza", "burger"]
}
player['fav_food'].append("noddle")
print(player['fav_food'])
~~~

>['pizza', 'burger', 'noddle']

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 21일 파이썬 스터디 공부

>for, pypi, requests

## for

~~~
website = (
  "google.com",
  "airbnb.com",
  "twitter.com",
  "facebook.com"
)

for potato in website:
  print("potato is equals to", potato)
~~~

>potato is equals to google.com<br>potato is equals to airbnb.com<br>potato is equals to twitter.com<br>potato is equals to facebook.com

~~~
websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

for website in websites:
  if website.startswith("https://"):
    print("good to go")
  else:
    print('we have to fix it')
~~~

>we have to fix it<br>we have to fix it<br>good to go<br>we have to fix it<br>good to go

## pypi

https://pypi.org/

>파이썬 모듈을 모아 놓은 사이트

## requests

라이브러리 다운로드하기 2.28.1

~~~
websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)

for website in websites:
  if not website.startswith("https://"): #if website.startswith("https://"): == False
    website = f"https://{website}"
  response = get(website)
  print(response)
  ~~~

  get은 웹사이트의 response를 return한다

  ><Response [200]><br><Response [200]><br><Response [200]><br><Response [200]><br><Response [200]>

  요청이 성공적으로 되었다는 뜻

  ~~~
  from requests import get
websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "https://tiktok.com"
)
results = {}
for website in websites:
  if not website.startswith("https://"): #if website.startswith("https://"): == False
    website = f"https://{website}"
  response = get(website)
  if response.status_code == 200:
    results[website] = "OK"
  else:
    results[website] = "FAILED"
print(results)
~~~

>{'https://google.com': 'OK', 'https://airbnb.com': 'OK', 'https://twitter.com': 'OK', 'https://facebook.com': 'OK', 'https://tiktok.com': 'OK'}


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 22일 파이썬 스터디 공부

>웹 스크래핑 기초, wwr, len

## WWR

https://weworkremotely.com/

~~~
https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=검색어
 # 예시
https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term=python
~~~

# 웹 스크래핑 기초

웹 사이트에 python 검색

~~~
from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  print(response.text)
~~~

성공적으로 웹 사이트에 request를 보냈을 때
~~~
...
        jQuery(this).parents('.outsider-select').find('select').trigger('chosen:open');    
      }
    });

    // Warning - Library is no longer maintained, refer: https://github.com/bbarakaci/fixto    // Update Library to https://cdnjs.com/libraries/stickybits
    var stickyEl = jQuery('#advanced_search_filters').fixTo('#side_filter_column', {       
      top: 100,
      mindBottomPadding: true
    });
  });
</script></body></html>
~~~

## beautifulsoup

request를 보낸 다음 받아온 텍스트에서 우리가 필요로 하는 데이터를 검색하기 위해서 필요함

~~~
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  print(soup.find_all('title'))
~~~

<br>title을 찾아서 출력함

~~~
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  print(soup.find_all('section', class_ = "jobs"))
~~~

section에서 class가 jobs인 것들을 출력함

~~~
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  print(soup.find_all('section', class_ = "jobs"))
~~~

~~~
[<section class="jobs" id="category-2"><article><h2><a href="/categories/remote-full-stack-programming-jobs">Full-Stack Programming Jobs</a><span class="latest_post">Latest post 5 days ago</span><a href="/categories/remote-full-stack-programming-jobs.rss"><img class="feed" height="16" src="https://
...
~~~

## len 

list, tuple의 길이를 준다

~~~
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_ = "jobs")
  print(len(jobs))
~~~

>2

## list

~~~
list_of_numbers = [1, 2, 3]

fisrt, second, third = list_of_numbers
print(fisrt, second, third)
~~~

>1 2 3

list의 순서를 안다면 내용 편집이 더 쉬워진다.



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 23일 파이썬 스터디 공부

>.string, selenium, 데이터 저장

태그 안의 문자열만 출력

## .string

~~~
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_ = "jobs")
  # print(len(jobs))
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)
    for post in job_posts:
      anchors = post.find_all('a')
      anchor = anchors[1]
      link = anchor['href']
      company, kind, region = anchor.find_all('span', class_ = "company")
      title = anchor.find('span', class_='title')
      print(company.string, kind.string, region.string, title.string)
~~~

>Proxify AB Full-Time Anywhere in the World Senior Python Engineer: Long-term job - 100% remote<br>Lemon.io Full-Time Latin America Only/Europe Only/UK Only/Canada Only Full-stack Developer (Python/React)<br>Trustworthy Full-Time Anywhere in the World Full Stack Software Engineer (React / Python)<br>OpenCraft Full-Time Anywhere in the World Senior Open Source Developer & DevOps (Python, Django, React, AWS/OpenStack)<br>NannyML Full-Time Anywhere in the World Senior Full-stack Engineer with Python<br>Optimile Full-Time Europe Only (Senior) Python Full Stack Software Developer<br>Input Logic Full-Time Canada Only Python Developer<br>Doximity Full-Time Americas Only Python Platform Engineer

## 데이터 저장

~~~
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  results = []
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_ = "jobs")
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)
    for post in job_posts:
      anchors = post.find_all('a')
      anchor = anchors[1]
      link = anchor['href']
      company, kind, region = anchor.find_all('span', class_ = "company")
      title = anchor.find('span', class_='title')
      job_data = {
        'company' : company.string,
        'region' : region.string,
        'position' : title.string
      }
      results.append(job_data)
  for result in results:
    print(result)
~~~

results라는 리스트에 job_data라는 딕셔너리들을 저장한다

### indeed 스크래퍼

우리가 만든 프로그램을 다른 파일에 저장하고 함수로 만들어서 main.py에 import 해서 사용한다<br>권한 문제로 403을 반한다. 때문에 selenium이라는 다른 라이브러리를 사용해서 스크래핑을 해야된다.

~~~
job_list.find_all('li', recursive=False)
~~~

>recursive=False<br>딱 한 단계 아래의 태그만 찾아낸다

## selenium

~~~
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no_sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)
browser.get("https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=1015284880e2ff62")
print(browser.page_source)
~~~


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 24일 파이썬 스터디 공부

>selenium, bs4, .select, 함수 호출

## indeed에서 bs4 사용하기

~~~
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from  extractors.wwr import extract_wwr_jobs

options = Options()
options.add_argument("--no_sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)
browser.get("https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=1015284880e2ff62")
soup = BeautifulSoup(browser.page_source, "html.parser")
~~~

## .select

~~~
anchor = job.select("h2 a")
~~~
>h2 태그 안에 있는 a를 찾는다.

## 페이지 수 확인하기

~~~
def get_page_count(keyword):
    options = Options()
    options.add_argument("--no_sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}&l=&from=searchOnHP&vjk=1015284880e2ff62")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", attrs={"aria-label": "pagination"})
    if pagination == None:
        return 1
    pages = pagination.select("div a")
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count
~~~

## 함수 호출

~~~
from extractors.wwr import extract_wwr_jobs
from extractors.indeed import get_page_count, extract_indeed_jobs
~~~

extractors 파일에 있는 get_page_count, extract_indeed_jobs 함수 불러오기



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 25일 파이썬 스터디 공부

>함수 호출, 파일 저장(csv), 과제

다른 웹 사이트 추출기 만들기, indeed에서 10개의  페이지를 스크랩 할 수는 코드 짜기

## 함수 호출

extractors 폴더 안에 indeed.py, wwr.py 파일 안에 있는 함수를 호출해서 사용

~~~
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

for job in jobs:
    print(job)
~~~


## 파일 저장

open("파일 이름", "모드"), w는 쓰기 모드이다.<br>write() 파일 안에 데이터 입력<br>close() 데이터 입력 후 파일 종료

~~~
keyword = input("What do you want to search for?")
file = open(f"{keyword}.csv", "w")
file.write("Position, Company, Location, URL")
file.close()
~~~

## csv

csv파일을 사용하려면 열을 쉼표로 행은 줄로 구분해야 된다.
~~~
{
    'link' : f"https://weworkremotely.com/{link}",
    'company' : company.string.replace(",", " "),
    'location' : region.string.replace(",", " "),
    'position' : title.string.replace(",", " ")
}
~~~

기존의 파일에서 쉼표가 들어가는 부분을 공백으로 처리하도록 replace 함수를 사용했음

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 26일 파이썬 스터디 공부

>함수, Flask, 변수, html

## 함수

파일 저장에 필요한 코드만 다른 파일에 따로 함수화 해서 저장<br>file.py 파일에 저장된 코드
~~~
def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Position, Company, Location, URL\n")
    for job in jobs:
        file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n")

    file.close()
~~~

main.py 코드

~~~
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword, jobs)
~~~

## Flask

서버 만들기

~~~
from flask import Flask
app = Flask("JobScrapper")
@app.route("/") #함수 위에 있어야 됨, decorator라고 함
def home():
    return 'hello world'
app.run("0.0.0.0")
~~~

## 변수

~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Scrapper</title>
</head>
<body>
    <h1>Hello to you! My name is {{name}}</h1>
    <a href="/hello">go to hello</a>
</body>
</html>
~~~

~~~
from flask import Flask, render_template

app = Flask("JobScrapper")
@app.route("/") #함수 위에 있어야 됨, decorator라고 함
def home():
    return render_template("home.html", name="asdf")  #변수로 넘기기
@app.route("/hello")
def hello():
    return "hello you!<br><a href='/'>go to main</a>"

app.run("0.0.0.0", debug=True)
~~~


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 27일 파이썬 스터디 공부

>request, arguments, 실습

## request

request는 브라우저가 웹사이트에 가서 콘텐츠를 요청하는 것을 말한다.<br>요청하는 URL이 무엇인지, IP주소가 무엇인지, Cookies를 가지고 있는지

### 실습 코드
~~~
from flask import Flask, render_template, request
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")
@app.route("/") #함수 위에 있어야 됨, decorator라고 함

def home():
    return render_template("home.html", name="asdf")

@app.route("/search")

def hello():
    keyword = request.args.get("keyword")
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = indeed + wwr
    return render_template("search.html", keyword = keyword, jobs=jobs)

app.run("0.0.0.0", debug=True)
~~~

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###  2023년 2월 28일 파이썬 스터디 공부

>pico

## pico

적은 양의 CSS로 페이지를 더 보기 좋게 만들어 준다.<br>https://picocss.com/docs/

~~~
<head>
    <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css">
</head>
~~~