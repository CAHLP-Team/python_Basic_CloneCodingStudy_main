print("\n")


#2023.02.17 Python 스터디 실습

# print("Hello world!")

# a = 2
# b = 3
# c = a + b
# print(c)

# my_name = "User012050"
# age = 99
# dead = False
# print("Hello my name is", my_name)
# print("and I'm ", age, " years old")

# def say_hello():
#   print("hello how r u?")
# say_hello()

# def say_hello(user_name, user_age):
#   print("hello", user_name,"how r u?")
#   print("you are", user_age, "years old")

# say_hello("User012050", 99)

# --------------------------------------------------------------------
#2023.02.18 Python 스터디 실습

# def say_hello(user_name = "User012050", user_age = 99):
#   print("hello", user_name,"how are you?")
#   print("you are", user_age, "years old")

# say_hello(False, 101) False출력
# say_hello(None, 101)  None출력
# say_hello(, 00) 에러

# def tax_cal(money):
#   return money * 0.35

# def pay_tax(tax):
#   print("Thank you for paying", tax)

# to_pay = tax_cal(100)
# pay_tax(to_pay)


# def tax_cal(money):
#   return money * 0.35

# def pay_tax(tax):
#   print("Thank you for paying", tax)

# pay_tax(tax_cal(100))


# def hello(word):
#   print(f"hello {word}")

# hello("User012050")


# if True:
#   print("it is True1")

# a = "abc"
# if a == "abc":
#   print("it is True2")

# a = 123
# if a > 10:
#   print("it is True3")


# if False:
#   print("it is True1")

# else:
#   print("it is False")


# winner = 10
# if winner > 10:
#   print("winner is greater than 10")
# elif winner == 10:
#   print("winner is 10")
# else:
#   print("winner is less than 10")

# --------------------------------------------------------------------
#2023.02.19 Python 스터디 실습

# input("How old are you?")


# age = input("How old are you?")
# print("user answer", age)


# age = input("How old are you?")
# print(type(age))


# age = int(input("How old are you?"))
# print(type(age))


# age = int(input("How old are you?"))
# if age < 18:
#   print("You can't drink.")
# elif age >= 18 and age <= 35:
#   print("You drink beer!")
# elif age == 60 or age == 70:
#   print("Birthday party!")
# else:
#   print("Go ahead!")


# True and  True == True
# False and True == False
# True and False == False
# False and False == False

# True or True == True
# True or False == True
# False or True == True
# False or False == False

# from random import randint

# user_choice = int(input("Choose number:"))
# pc_choice = randint(1, 50)

# if user_choice == pc_choice:
#   print("You win!")
# elif user_choice >  pc_choice:
#   print("Lower! Computer chose", pc_choice)
# elif user_choice < pc_choice:
#   print("Higher! Computer chose", pc_choice)


# distance = 0
# while distance < 20:
#   print("I'm running:", distance,"km")
#   distance = distance + 1


# from random import randint

# print("Welcom to Python Casino")
# pc_choice = randint(1, 50)

# playing = True
# while playing:
#   user_choice = int(input("Choose number:"))
#   if user_choice == pc_choice:
#     print("You win!")
#     playing = False
#   elif user_choice >  pc_choice:
#     print("Lower!")
#   elif user_choice < pc_choice:
#     print("Higher!")


# --------------------------------------------------------------------
#2023.02.20 Python 스터디 실습

# days_of_week = ["mon", "Tue", "Wed", "Thur", "Fri"]

# print(days_of_week)

# name = "abc"
# print(name.upper())


# name ="nico"
# print(name.capitalize())


# name = "nico"
# print(name.replace("o", "><"))


# name = "nico"
# print(name.endswith("f"))


# print("nico".endswith("f"))

# days_of_week = ["mon", "Tue", "Wed", "Thur", "Fri"]
# print(days_of_week)
# # days_of_week.clear()
# # days_of_week.reverse()
# days_of_week.append("Sun")
# days_of_week.remove("Fri")
# print(days_of_week)


# days_of_week = ["mon", "Tue", "Wed", "Thur", "Fri"]
# print(days_of_week[3])


# days_of_week = [1, 2, 3, True, False, "hi", "black", [ 1, 2, 3, [False, True]]]
# print(days_of_week[7][3][1])


# days = ("Mon", "Tue", "Wed")
# days.append("Fri")


# player = {
#   'name' : 'nico', 
#   'age' : 12,
#   'alive' : True,
#   'fav_food' : ["pizza", "burger"]
# }
# player.pop('age')
# print(player)


# player = {
#   'name' : 'nico', 
#   'age' : 12,
#   'alive' : True,
#   'fav_food' : ["pizza", "burger"]
# }
# player['xp'] = 1500
# print(player)


# player = {
#   'name' : 'nico', 
#   'age' : 12,
#   'alive' : True,
#   'fav_food' : ["pizza", "burger"]
# }
# player['fav_food'].append("noddle")
# print(player['fav_food'])


# --------------------------------------------------------------------
#2023.02.21 Python 스터디 실습

# websites = (
#   "google.com",
#   "airbnb.com",
#   "https://twitter.com",
#   "facebook.com",
#   "https://tiktok.com"
# )

# for website in websites:
#   if website.startswith("https://"):
#     print("good to go")
#   else:
#     print('we have to fix it')


# websites = (
#   "google.com",
#   "airbnb.com",
#   "https://twitter.com",
#   "facebook.com",
#   "https://tiktok.com"
# )

# for website in websites:
#   if not website.startswith("https://"): #if website.startswith("https://"): == False
#     website = f"https://{website}"
#   print(website)


# from requests import get
# websites = (
#   "google.com",
#   "airbnb.com",
#   "https://twitter.com",
#   "facebook.com",
#   "https://tiktok.com"
# )
# results = {}
# for website in websites:
#   if not website.startswith("https://"): #if website.startswith("https://"): == False
#     website = f"https://{website}"
#   response = get(website)
#   if response.status_code == 200:
#     results[website] = "OK"
#   else:
#     results[website] = "FAILED"
# print(results)


# --------------------------------------------------------------------
#2023.02.22 Python 스터디 실습

# from requests import get

# base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# search_term = "python"
# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#   print("Can't request website")
# else:
#   print(response.text)


# from requests import get
# from bs4 import BeautifulSoup

# base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# search_term = "python"
# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#   print("Can't request website")
# else:
#   soup = BeautifulSoup(response.text, "html.parser")
#   print(soup.find_all('section', class_ = "jobs"))


# from requests import get
# from bs4 import BeautifulSoup

# base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# search_term = "python"
# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#   print("Can't request website")
# else:
#   soup = BeautifulSoup(response.text, "html.parser")
#   jobs = soup.find_all('section', class_ = "jobs")
#   print(len(jobs))
#   for job_section in jobs:
#     job_posts = job_section.find_all('li')
#     job_posts.pop(-1)
#     for post in job_posts:
#       print(post)
#       print("//////////////////")


# from requests import get
# from bs4 import BeautifulSoup

# base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# search_term = "python"
# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#   print("Can't request website")
# else:
#   soup = BeautifulSoup(response.text, "html.parser")
#   jobs = soup.find_all('section', class_ = "jobs")
#   # print(len(jobs))
#   for job_section in jobs:
#     job_posts = job_section.find_all('li')
#     job_posts.pop(-1)
#     for post in job_posts:
#       # print(post)
#       anchors = post.find_all('a')
#       anchor = anchors[1]
#       print(anchor['href'])


# list_of_numbers = [1, 2, 3]

# fisrt, second, third = list_of_numbers
# print(fisrt, second, third)



# from requests import get
# from bs4 import BeautifulSoup

# base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# search_term = "python"
# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#   print("Can't request website")
# else:
#   soup = BeautifulSoup(response.text, "html.parser")
#   jobs = soup.find_all('section', class_ = "jobs")
#   # print(len(jobs))
#   for job_section in jobs:
#     job_posts = job_section.find_all('li')
#     job_posts.pop(-1)
#     for post in job_posts:
#       anchors = post.find_all('a')
#       anchor = anchors[1]
#       link = anchor['href']
#       company, kind, region = anchor.find_all('span', class_ = "company")
#       title = anchor.find('span', class_='title')
#       print(company, kind, region, title)
#       print("//////////////////")
#       print("//////////////////")


# --------------------------------------------------------------------
#2023.02.23 Python 스터디 실습

# from requests import get
# from bs4 import BeautifulSoup

# base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# search_term = "python"
# response = get(f"{base_url}{search_term}")

# if response.status_code != 200:
#   print("Can't request website")
# else:
#   results = []
#   soup = BeautifulSoup(response.text, "html.parser")
#   jobs = soup.find_all('section', class_ = "jobs")
#   for job_section in jobs:
#     job_posts = job_section.find_all('li')
#     job_posts.pop(-1)
#     for post in job_posts:
#       anchors = post.find_all('a')
#       anchor = anchors[1]
#       link = anchor['href']
#       company, kind, region = anchor.find_all('span', class_ = "company")
#       # print(company, kind, region)
#       title = anchor.find('span', class_='title')
#       job_data = {
#         'link' : f"https://weworkremotely.com/{link}",
#         'company' : company.string,
#         'region' : region.string,
#         'position' : title.string
#       }
#       results.append(job_data)
#   for result in results:
#     print(result)


# from requests import get
# from bs4 import BeautifulSoup
# from  extractors.wwr import extract_wwr_jobs

# search_term = "python"
# # base_url_1 = f"https://kr.indeed.com/jobs?q={search_term}"
# base_url_1 = f"https://kr.indeed.com/jobs?q={search_term}&l=&vjk=1015284880e2ff62"

# response = get(base_url_1)
# # print(response.status_code) #403 출력
# # if response.status_code != 200:
# #   print("Can't request page")
# # else:
# # 권한 문제로 200 코드를 받을 수 없다
# # print(response.text)

# soup = BeautifulSoup(response.text, "html.parser")
# job_list = soup.find('ul', class_ = "jobsearch-ResultsList css-0")
# jobs = job_list.find_all('li', recursive=False)
# for job in jobs:
#   print(job)

# from requests import get
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("--no_sandbox")
# options.add_argument("--disable-dev-shm-usage")
# browser = webdriver.Chrome(options=options)
# browser.get("https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=1015284880e2ff62")
# print(browser.page_source)


# --------------------------------------------------------------------
#2023.02.24 Python 스터디 실습

# from requests import get
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# from extractors.wwr import extract_wwr_jobs
# from extractors.indeed import get_page_count, extract_indeed_jobs


# jobs = extract_indeed_jobs("python")
# print(len(jobs))


# --------------------------------------------------------------------
#2023.02.25 Python 스터디 실습

# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs

# keyword = input("What do you want to search for?")
# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)

# jobs = indeed + wwr

# for job in jobs:
#     print(job)
    

# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs

# keyword = input("What do you want to search for?")

# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)

# jobs = indeed + wwr

# for job in jobs:
#     print(job)

# file = open(f"{keyword}.csv", "w")
# file.write("Position, Company, Location, URL\n")

# for job in jobs:
#     file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n")

# file.close()

# --------------------------------------------------------------------
#2023.02.26 Python 스터디 실습

# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs
# from file import save_to_file

# keyword = input("What do you want to search for?")

# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# jobs = indeed + wwr

# save_to_file(keyword, jobs)


# from flask import Flask, render_template

# app = Flask("JobScrapper")
# @app.route("/") #함수 위에 있어야 됨, decorator라고 함
# def home():
#     return render_template("home.html", name="asdf")
# @app.route("/search")
# def hello():
#     return render_template("search.html")

# app.run("0.0.0.0", debug=True)


# --------------------------------------------------------------------
#2023.02.27 Python 스터디 실습

# from flask import Flask, render_template, request
# from extractors.indeed import extract_indeed_jobs
# from extractors.wwr import extract_wwr_jobs

# app = Flask("JobScrapper")
# @app.route("/") #함수 위에 있어야 됨, decorator라고 함

# def home():
#     return render_template("home.html", name="asdf")

# @app.route("/search")

# def hello():
#     keyword = request.args.get("keyword")
#     indeed = extract_indeed_jobs(keyword)
#     wwr = extract_wwr_jobs(keyword)
#     jobs = indeed + wwr
#     return render_template("search.html", keyword = keyword, jobs=jobs)

# app.run("0.0.0.0", debug=True)


# --------------------------------------------------------------------
#2023.02.28 Python 스터디 실습

from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file
app = Flask("JobScrapper")

db = {}

@app.route("/") #함수 위에 있어야 됨, decorator라고 함

def home():
    return render_template("home.html")

@app.route("/search")

def hello():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword = keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")   
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

# app.run("0.0.0.0", debug=True)
app.run("0.0.0.0")