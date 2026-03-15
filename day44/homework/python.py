#1) დაწერეთ ფუნქცია, სახელად calculateArea, რომელიც არგუმენტად მიიღებს ოთხკუთხედის სიგრესა და სიგანეს და დააბრუნებს მის ფართობს.
#  შედეგი გამოიტანეთ ტერმინალში.

def calculatearea (Length, Width):
    return Length * Width

print(calculatearea (5, 6))


# 2) დაწერეთ ფუქნცია, რომელიც პარამეტრად მიიღებს იმ რაოდენობას, რამდენჯერად უნდა დაიპრინტოს "Hello, World".

def hello_world (n):
    for i in range(n):
        print("hello world")


(hello_world(6))


# 3) დაწერეთ ფუქნცია, სახელად celsiusToFahrenheit, რომელიც პარამეტრად მიიღებს ცელსიუსს და გადაიყვანს ფარენჰეიტში. ფორმულა - (Celsius * 9/5) + 32

def celsiusToFahrenheit (Celsius):
    return (Celsius * 9/5) + 32 

print(celsiusToFahrenheit(0))

print(celsiusToFahrenheit(9))


#4) დაწერეთ ფუნქცია სახელად sumDigits, რომელიც არგუმენტად იღებს რიცხვს და აბრუნებს მისი ციფრების ჯამს.


def sumDigits (nam):
    total=0
    for i in str(nam):
        total+=int(i)
    return total
    
print(sumDigits(1234567890))   


# 5) დაწერეთ ფუნქცია სახელად countBs, რომელიც იღებს სტრიქონს თავის ერთადერთ არგუმენტად და აბრუნებს სტრიქონში 
# დიდი "B" სიმბოლოების რაოდენობას.

def countBs(s):
    count = 0
    for i in s:
        if i.upper() == "B": 
            count += 1
    return count

print(countBs("evnbiubbgfbubuhbbbtrb"))  


def countBs(str):
    count = 0
    for i in str:
        if i == "B":        
            count += 1
    return count

print(countBs("evnbiubbgfbubuhbbbtrbBBB"))



#6) დაწერეთ ფუნქცია, რომელიც მიიღებს ორ პარამეტრს და დააჯამებს ყველა რიცხვს გარკვეულ შუალედში. მაგალითად შეკრიბავს რიცხვებს 5-დან 100-მდე.

def sum (Start, finish):
    total=0
    for i in range(Start, finish+1):
        total+=i
    return total

print(sum(1,13)) 


#7)გამოიყენეთ for loop 1-დან 30-მდე 3-ის ჯერადების დასაბეჭდად.

for i in range(1,31):
    if i % 3 == 0:
        print(i)



#8) გამოიყენეთ for loop 4-ის გამრავლების ცხრილის დასაბეჭდად (4 × 1-დან 4 × 10-მდე).    
  
for i in range(1, 11):      
    print(f"4 x {i} = {4*i}")



#9) გამოიყენეთ for loop 20-დან 10-მდე რიცხვების დასაბეჭდად.

for i in range(20,9,-1):
    print(i)


 


#11) დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და დაბეჭდოს "Hello!" იმდენჯერ რამდენსაც უდრის ეს შეყვანილი რიცხვი.

User=int(input("Enter a number to print Hello World :"))

for i in range(1,User + 1):
    print("Hello world")




    

    










        




