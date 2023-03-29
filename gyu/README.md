## Python Study 

## 파이썬 스터디 1일차

|날짜|제목|설명|링크|
|-|-|-|-|
23.02.17|파이썬 기초|변수 및 함수 설명, parameter 개념

### 필기
+ 변수 => 변수명 = 내용
+ 변수명에는 빈공간이 있으면 안되므로 camel case(myAge), snake case(my_age) 스타일을 주로 사용
+ 변수명은 숫자, 특수문자로 시작하지 않는다.
+ " " => 문자열
+ boolean => 참(True) 또는 거짓(False)
+ function => def 펑션이름():

### 실습

~~~
def say_hello(name):
  print("hello",name, "how r u?")
say_hello("jg")

 #name => parameter
 #jg => argument
~~~

~~~
def multi(name, age):
 print("hello",name)
 print("you are", age, "years old") 
multi("jg", 23)

 #함수의 갯수와 순서에 유의
~~~

## 파이썬 스터디 2일차

|날짜|제목|설명|링크|
|-|-|-|-|
23.02.18|파이썬 기초2|복습, 파라미터 기본값 설정, 리턴문, 조건문

### 복습
+ 함수 => 작성후 몇번이고 재사용 가능한 코드
+ 파라미터 => 함수 안으로 데이터를 보내 함수의 결과를 바꿀 수 있게 하는것

### 학습내용 (실습 포함)

+ 파라미터 기본값 설정
~~~
def say_hello(name="anonymous"):
 print("hello", name)
say_hello()
~~~

+ 과제(계산기)
~~~
def plus(a="0", b="0"):
  print(a + b)
plus(8, 2)
plus()
 # =10 (더하기)

def minus(a="0", b="0"):
  print(a - b)
minus(8, 2)
 # =6 (빼기)

def mltp(a="0", b="0"):
  print(a * b)
mltp(8, 2)
 # =16 (곱하기)

def dvsn(a="0", b="0"):
  print(a / b)
dvsn(8, 2)
 # =4 (나누기)

def pwo(a="0"):
  print(a**2)
pwo(8)
 # =64 (제곱)
~~~


+ return문: 함수 바깥으로 값을 보내줌. 그리고 함수 종료
~~~
 #실습1(세금 계산기)
def tax_calc(money):
 return money * 0.35

def pay_tax(tax):
  print("thank yo for paying", tax)
  
pay_tax(tax_calc(1500000))
 # 실습 설명: tax_calc의 리턴값을 받아서 pay_tax의 프린트문 수행
~~~

+ 문자열에 변수 추가하는 법 => f "~~" { }
~~~
name = "jg"
age = 23
eyesclr = "black"

print(f"hello I'm {name}, i have {age} years in the earth, {eyesclr} is my eye color")
~~~

~~~
 #실습2(주스메이커)-return문, 문자열 변수추가법 활용
def make_juice(fruit):
  return f"{fruit}+🥤"

def add_ice(juice):
  return f"{juice}+🧊"

def add_sugar(iced_juice):
  return f"{iced_juice}+🍭"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)

 #실습 설명
1) make_juice를 통해 사용자가 입력한 fruit가 fruit+🥤 으로 리턴
2) add_ice를 통해 만들어진 jucie 값에 🧊이 플러스 되어 juice+🧊으로 리턴
3) add_sugar를 통해 얼음이 추가된 jucie (iced_juice)에 🍭이 플러스 되어 iced_juice+🍭가 리턴
4) 마지막 네줄은 1~3을 차례로 실행시켜 출력시킴 (결과: 🍎+🥤+🧊+🍭)
~~~

+ if문 - if문의 조건이 참이면 코드 실행
  else문 - if문의 조건이 틀릴 시 실행
  elif문 - 여러 조건 확인 시 사용
  참고: if문의 조건이 참일시 그 뒤의 elif, else 문의 조건들은 확인안함
~~~
 #if문 실습
winner = 10

if winner > 10:
  print("winner is greater than 10")
  
elif winner < 10: #if문 조건 외에 다른 조건 확인, 조건참이면 뒤의 조건들은 확인안함
  print("winner is less than 10")

else: #winner = 10, 모든 경우가 false 일때
  print("winner is 10")
 #결과: winner is 10 (winner변수가 10이므로 if문과 elif문은 거짓, 따라서 else문 작동)
~~~



## 파이썬 스터디 3일차

### 필기
+ input => 하나의 argument를 받음, 사용자의 입력값이 리턴값

+ type => 입력값의 타입 출력
+ print(type(입력값))

+ and => 동시에 두 조건을 확인, 모두 참이여야만 true
  true and true = true
  true and false = false
  false and true = false
  false and false = false

+ or => 앞부분 또는 뒷부분이 참인지 확인(하나만 참이어도 됨)
  true or true = true
  true or false = true
  false or true = true
  false or false = false

+ 파이썬에는 다양한 함수를 포함한 모듈이 있고, 필요시 이를 import하여 사용 가능하다!

+ while => 조건을 만족하면 코드를 무한히 반복

### 실습
~~~
 #실습1(파이썬 카지노) 
from random import randint
print("welcome to python casino!")

pc_choice = randint(0, 100)

playing = True

while playing:
 
 user_choice = int(input("choose number(1~100).: "))

 if user_choice == pc_choice:
   print("you won!")
   playing = False

 elif user_choice > pc_choice:
   print("lower!")

 elif user_choice < pc_choice:
   print("higher!")
~~~


## 파이썬 스터디 4일차

### 필기 및 실습

+ 메소드 => 데이터와 결합된 function
+ 데이터.메소드명()
+ 매우 다양함 [startswith(첫글자 확인), endswith(끝글자 확인), replace(교체), upper(대문자로 교체),count(수 세기), clear(리스트 내용 모두 삭제), append(리스트에 내용 추가) 등]
~~~
 #실습
name = "jg"
name.upper()
~~~

+ 리스트 => 이름=[내용], 어떤 형식이든 넣을 수 있음
~~~
days = ["mon", "tue", "wed"]
print(days[0])
~~~

+ 튜플 => 이름(내용), 리스트와 다르게 불변성을 가짐(변경 불가), 아이템에 접근할땐 대괄호 사용
~~~
days2 = ("mon", "tue", "wed")
print(days2[0])
~~~

+ dictionary => 이름={내용}, 인덱스를 써야하는 리스트와는 다르게 키-값 쌍으로 이루어져 있기 때문에 키를 통해 값 호출 가능
~~~
player = {
    'name' : 'jg',
    'age' : 23,
    'alive' : True,
    'fav_food' : ['cola', 'apple']
}

print(player['age']) #player 딕셔너리의 age 출력
player['fav_food'].append("noodle") #player 딕셔너리의 fav_food 리스트에 noodle 추가
~~~


## 파이썬 스터디 5일차
### 필기 및 실습

~~~
from requests import get

websites = (
    "https://google.com",
    "naver.com",
    "twitter.com",
    "facebook.com"
)

results={}

for website in websites: #리스트(투플) 내 각 아이템에 대하여 코드 실행
  if not website.startswith("https://"): #website가 https://로 시작하지 않으면
   website = f"https://{website}" #website에 https://를 붙임
  # print(website)
  response = get(website) #get함수는 웹사이트의 응답을 리턴
  if response.status_code == 200: #staus code => 결과에서 상태(숫자)만 리턴함
    results[website]  =  "ok" #새로운 키(해당하는 website)를 results 닥셔너리에 추가, ok라고 정의(=)
  else:   
    results[website]  =  "failed"

print(results) 
~~~

+ 참고: Pypi는 라이브러리를 검색할 수 있는 웹 사이트이다.


## 파이썬 스터디 6일차
### 필기 및 실습

~~~
from requests import get
from bs4 import BeautifulSoup #beatifulsoup => 웹사이트(html)의 데이터를 받아올수 있게 해주는 라이브러리

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=✓&term="
search_term = "python"

response = get(f"{base_url}{search_term}") #주소(base_url + search_term)의 응답을 받아옴

if response.status_code != 200:
    print("can't request website")

else:
    soup = BeautifulSoup(response.text, "html.parser") # html.parser => html을 보내준다고 beatifulsoup에 전달
    jobs = soup.find_all('section', class_="jobs")
     #section(직업 전체) => li(직업 기업별로 분류) => anchor(직업 정보)
     #section 중 class가 jobs인 section의 내용을 가져옴
     #class_="jobs" => keyword argument(순서(위치)를 신경 쓰지 않는 경우)
    for job_section in jobs:
        job_posts = job_section.find_all("li") #모든 li(직업 리스트)를 찾아냄
        job_posts.pop(-1) #job list에서 마지막 항목 제거(view all 버튼이 출력되지 않도록 함)
        for post in job_posts: #job posts에서 anchors를 추출하고, anchors에서 href 저장 및 company가 들어간 span(세부 정보)를 추출(li 수대로 반복)
            anchors = post.find_all('a') #job_posts에서 anchor를 찾아냄
            anchor = anchors[1] #두번째 anchor가 필요하기 때문에 두번째 항목을 달라고 요청
            link = anchor['href']
            company, kind, region = anchor.find_all('span', class_="company") #span 클래스 중 company가 들어간 클래스를 차례로 추출
            title = anchor.find('span', class_ = 'title')
            print(company, kind, region, title)
            print("/////////////////")
            print("/////////////////")
~~~

## 파이썬 스터디 7일차
### 필기 및 실습

+ weworkremotely용 웹스크래퍼 완성
  1. 정보 저장 및 함수화
~~~
from requests import get
from bs4 import BeautifulSoup #beatifulsoup => 웹사이트(html)의 데이터를 받아올수 있게 해주는 라이브러리

def extract_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?utf8=✓&term="
  keyword

  response = get(f"{base_url}{keyword}") #주소(base_url + keyword)의 응답을 받아옴

  if response.status_code != 200:
    print("can't request website")

  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser") # html.parser => html을 보내준다고 beatifulsoup에 전달, response.text => 웹사이트의 코드, beatifulsoup => response.text를 받아와서 python의 데이터 구조로 변환
    jobs = soup.find_all('section', class_="jobs") #section(직업 전체) => li(직업 기업별로 분류) => anchor(직업 정보)
                                                   #section 중 class가 jobs인 section의 내용을 가져옴
                                                   #class_="jobs" => keyword argument(순서(위치)를 신경 쓰지 않는 경우)
    for job_section in jobs:
        job_posts = job_section.find_all("li") #모든 li(직업 리스트)를 찾아냄
        job_posts.pop(-1) #job list에서 마지막 항목 제거(view all 버튼이 출력되지 않도록 함)
        for post in job_posts: #job posts에서 anchors를 추출하고, anchors에서 href 저장 및 company가 들어간 span(세부 정보)를 추출(li 수대로 반복)
            anchors = post.find_all('a') #job_posts에서 anchor를 찾아냄
            anchor = anchors[1] #두번째 anchor가 필요하기 때문에 두번째 항목을 달라고 요청
            link = anchor['href']
            company, kind, region = anchor.find_all('span', class_="company") #span 클래스 중 company가 들어간 클래스를 차례로 추출
            title = anchor.find('span', class_ = 'title')
            job_data = {  #글자만을 추출하여 job_data 딕셔너리에 저장
                'link': f"https://weworkremotely.com/{link}",
                'company': company.string,
                'region': region.string,
                'position': title.string
            }
            results.append(job_data)
    for result in results:
        return results     
~~~

 2. 함수 사용
 ~~~
 from requests import get
 from bs4 import BeautifulSoup 
 from extractors.study6 import extract_jobs

 jobs = extract_jobs("python") #검색하고자 하는 단어 입력
 print(jobs)
 ~~~

+ indeed용 웹스크래퍼

~~~
from bs4 import BeautifulSoup
from selenium import webdriver #셀레니움
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("http://www.indeed.com/jobs?q=python&limit=50")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all('li', recursive=False) #recursive=False => ul 바로 아래의 Li만 찾기 위해서
for job in jobs:
    zone = job.find("div", class_ = "mosaic-zone")

    if zone == None: #직업 정보를 li 안에 있다면 (NONE => 무언가 없을 때))
     print("job li")
~~~


## 파이썬 스터디 8일차
### 필기 및 실습

+ indeed를 활용한 웹스크래퍼 제작 완료 및 함수 정의

~~~

from bs4 import BeautifulSoup
from selenium import webdriver #셀레니움
from selenium.webdriver.chrome.options import Options

def get_page_count(keyword): #페이지 수 세기(스크래핑 해야할 페이지 수 세기)
    options = Options()
    options.add_experimental_option("detach", True)
    response = webdriver.Chrome(options=options)

    base_url = "https://www.indeed.com/jobs?q="
    response.get(f"{base_url}{keyword}")


    soup = BeautifulSoup(response.page_source, "html.parser")
    pagination = soup.find("ul", class_ = "pagination-list")

    if pagination == None:
        return 1 #pagination이 None이면(페이지가 하나밖에 없으면) 1을 리턴
    
    pages = pagination.find("li", recursive=False)

    count = len(pages)

    if count >= 5:
        return 5
    
    else:
        return count
    
-------------------------------------------------------------------

def extract_indeed_jobs(keyword): #페이지 별로 직업정보 스크래핑을 반복 
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages): #range => 순서 객체를 리턴해주는 함수(즉시 List를 생성)

        options = Options()
        options.add_experimental_option("detach", True)
        response = webdriver.Chrome(options=options)
        
        base_url = "https://www.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting", final_url)
        response.get(final_url)

        soup = BeautifulSoup(response.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False) #recursive=False => ul 바로 아래의 Li만 찾기 위해서
        for job in jobs:
            zone = job.find("div", class_ = "mosaic-zone")

            if zone == None: #직업 정보를 li 안에 있다면 (NONE => 무언가 없을 때))
                    #  h2 = job.find("h2", class_="jobTitle") 
                    #  a = h2.find("a")
                anchor = job.select_one("h2 a") #h2를 선택하여 들어간 다음, a를 가진 리스트 하나만 가져와라.
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")

                job_data = {
                    'link': f"https://www.indeed.com{link}",
                    'company': company.string,
                    'location': location.string,
                    "postion": "" #aria label
                    }
                results.append(job_data)
    return results
~~~


## 파이썬 스터디 9일차
### 필기 및 실습
~~~
 #만들었던 함수 호출하여 결과 저장하기

from requests import get
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from extractors.study7 import extract_indeed_jobs
from extractors.study6 import extract_jobs

keyword = input("what do you want to search for?")

indeed = extract_indeed_jobs(keyword)
extj = extract_jobs(keyword)

jobs = indeed + extj

def save_to_file(file_name, jobs):

    file = open(f"{file_name}.csv", "w") #csv로(입력된 keyword를 제목으로) 저장(쓰기 전용으로) => 이름과 모드 설정
    file.write("Position, Company, Location, URL\n") #Position, Company, Location, URL을 쉼표로 구분하여 열마다 삽입 후 줄바꿈
    for job in jobs:
        file.write(f"{job['position']}, {job['company']}, {job['location']},{job['link']}\n") # 스크랩한 정보(Position, Company, Location, URL)를 열마다 삽입 후 줄바꿈

    file.close()
~~~

## 파이썬 스터디 10일차
### 필기 및 실습

+ flask 기본 및 실습
~~~
 #flask => 파이썬을 이용해서 웹사이트를 구축할 수 있는 초소형 프레임워크

from flask import Flask, render_template

app = Flask("jobscrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def hello():
    return render_template("search.html")


app.run("127.0.0.1")
~~~

+ html 다루기(기본 템플릿 사용)
~~~
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta http-equiv="X-UA-Compatible" contents="IE=edge">
 <meta name="viewport" content="width=device-width,
 initial-scale=1.0">
 <title>job scrapper</title>

</head>
<body>
<h1>Search Results:</h1>
<h4>What job do you want?</h4>
<form action="/search"> 
    <input type = "text" name = "keyword" placeholder = "Write keyword please" />
    <button>Search</button>
</form>
</body>
</html>
~~~

## 파이썬 스터디 11일차
### 필기 및 실습

+ main.py 부분(exract_indeed_jobs, extract_jobs 함수를 추가하여 직업정보 받아오도록 함)
~~~
from flask import Flask, render_template, request
from extractors.study7 import extract_indeed_jobs
from extractors.study6 import extract_jobs

app = Flask("jobscrapper")

@app.route("/")
def home():
    return render_template("home.html", name = "jg")

@app.route("/")
def search():
    keyword = request.args.get("keyword")
    indeed = extract_indeed_jobs(keyword)
    ijs = extract_jobs(keyword)
    jobs = indeed + ijs
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("127.0.0.1")
~~~

+ serach.html 부분(받아온 직업정보를 띄우는 기능 추가)
 필기
 1) flask에서 for문을 사용하는 방식 => {% for~~ %} RmxsofEosms {% endfor %}
 2) {{}} 문법과 {%%}문법의 차이 => {{}}안에 변수를 넣으면  flsak가 변수를 값으로 변환, {%%}은 실행하고자 하는 파이썬 코드를 입력
 3) 코드에 있는 for문 설명 => flask가 {{}}안에 있는 걸(position, company 등) 데이터로 변환
~~~
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta http-equiv="X-UA-Compatible" contents="IE=edge">
 <meta name="viewport" content="width=device-width,
 initial-scale=1.0">
 <title>job scrapper</title>

</head>
<body>
<h1>Search Results for "{{keyword}}":</h1>

{% for job in jobs %} 
<div>
    <span>{{job.position}}</span>
    <span>{{job.company</span>
    <span>{{job.location}}</span>
    <a href = "{{job.link}}" target = "_blank">Apply now &rarr;</a>
</div>
{% endfor %}

<h4>What job do you want?</h4>
<form action="/search"> 
    <input type = "text" name = "keyword" placeholder = "Write keyword please" />
    <button>Search</button>
</form>
</body>
</html>
~~~

## 파이썬 스터디 12일차
### 필기 및 실습

+ main.py(파일 다운 기능 추가)
~~~
from flask import Flask, render_template, request, redirect, send_file
from extractors.study7 import extract_indeed_jobs
from extractors.study6 import extract_jobs
from study7_1 import save_to_file
app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None: #아무것도 검색하지 않았을 때
       return redirect("/") #다시 돌려보냄
    if keyword in db:
     jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        ijs = extract_jobs(keyword)
        jobs = indeed + ijs
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
   keyword = request.args.get("keyword")
   if keyword == None:
      return redirect("/")
   if keyword not in db:
      return redirect(f"/search?keyword={keyword}")
   save_to_file(keyword, db[keyword]) #파일 저장
   return send_file(f"{keyword}.csv", as_attachment=True)

app.run("0.0.0.0")
~~~

+ home.html(pico, table을 활용하여 이쁘게 만들기)
~~~
<!DOCTYPE html>
<html lang="en">

<head>
 <meta charset="UTF-8">
 <meta http-equiv="X-UA-Compatible" contents="IE=edge">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>job scrapper</title>
 <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css">
</head>

<body>
 <main class = "container">
    <h1>Job Scrapper</h1>
    <h4>What job do you want?</h4>
    <form action="/search" method="get">
        <input type = "text" name = "keyword" placeholder = "Write keyword please" />
        <button>Search</button>
    </form>>
 </main>
</body>

</html>
~~~

+ search.html(pico, table을 활용하여 이쁘게 만들기)
~~~
<!DOCTYPE html>
<html lang="en">

<head>
 <meta charset="UTF-8">
 <meta http-equiv="X-UA-Compatible" contents="IE=edge">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Job Scrapper</title>
 <link rel="stylesheet" href="https://unpkg.com/@picocss/pico@1.*/css/pico.min.css">
</head>

<body>
    <main class = "container">    
        <hgroup>
         <h1>Search Results for "{{keyword}}":</h1>
         <a target="_blank" href="/export?keyword={{keyword}}">Export to file</a>"
         <a target="_blank" href="/">Go to home</a>
        </hgroup>

        <table role = "grid">
            <thread>
                <tr>
                    <th>Position</th>
                    <th>Company</th>
                    <th>Location</th>
                    <th>Link</th>
                </tr>
            </thread>

            <tbody>
            {% for job in jobs %} 
                <tr>
                    <td>{{job.position}}</td>
                    <td>{{job.company}}</td>
                    <td>{{job.location}}</td>
                    <td><a href = "{{job.link}}" target = "_blank">Apply &rarr;</a></td>
                </tr>
            {% endfor %}  
            </tbody>
            <figure></figure>
        </table>
    </main>
</body>

</html>
~~~