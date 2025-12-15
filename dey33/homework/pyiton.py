#1) დაწერეთ ფუნქცია, სახელად sum, რომელიც არგუმენტებად მიიღებს ორ რიცხვს და დააბრუნებს მათ ჯამს. შედეგი გამოიტანეთ ტერმინალში.

def sum (a,b):
    return a + b

print(sum(666,999))


# 2) დაწერეთ ფუქნცია, რომელიც პარამეტრად მიიღებს იმ რაოდენობას, რამდენჯერად უნდა გამოკონსოლდეს "Hello, World".

def text(Hello_World=3): 
    for _ in range(Hello_World):
        print("Hello World")

text(Hello_World=3)
        

# 3) დაწერეთ ფუნქცია სახელად countBs, რომელიც იღებს სტრიქონს თავის ერთადერთ არგუმენტად და 
# აბრუნებს სტრიქონში დიდი "B" სიმბოლოების რაოდენობას.


def countBs (text):
    count=0
    for i in text:
        if i == "b":
            count+=1

    return count

result=countBs("bubblebush") 
print(result)



#4) დაწერეთ ფუნქცია, რომელიც მიიღებს ორ პარამეტრს და დააჯამებს ყველა რიცხვს გარკვეულ შუალედში.
#  მაგალითად შეკრიბავს რიცხვებს 5-დან 100-მდე.

def Sum_of_all_numbers(start, end):
    for i in range(start, end):
        print(i, "+", i + 1, "=", i + (i + 1))

Sum_of_all_numbers(5, 100)



#5) შექმენით ფუნქცია, რომელიც მოგთხოვთ სიტყვის ან წინადადების (string) შეყვანას და შემდეგ გიჩვენებთ,
#  თუ რამდენი სიმბოლოსგან შედგება თქვენი ჩანაწერი.


def text_input (text):
    text=input("Enter Text: ")
    print(f"თქვენი შეყვანილი ტექსტი შედგება {len(text)} სიმბოლოსგან  :")


text_input(text)



# 6) შექმენით ფუნქცია, რომელიც დააბრუნებს მასივში არსებული რიცხვების საშუალო არითმეტიკულს.

def Arithmetic_mean():
    numbers = [777, 10, 666, 999]
    total = 0

    for num in numbers:
        total += num

    count = len(numbers)          
    average = total / count
    print("საშუალო არითმეტიკული:", average)

Arithmetic_mean()

 




        







    


