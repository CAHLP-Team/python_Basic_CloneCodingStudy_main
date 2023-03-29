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
  
