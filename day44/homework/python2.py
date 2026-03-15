#10) დაწერეთ პროგრამა, რომელიც გამოთვლის კენტი რიცხვების ჯამს 1-დან 100-მდე და დაბეჭდავს შედეგს.

total=0

for i in range(1, 101):
    if i % 2 == 1:
        total+=i

print(total)     

#11) დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და დაბეჭდოს "Hello!" იმდენჯერ რამდენსაც უდრის ეს შეყვანილი რიცხვი.

User=int(input("Enter a number to print Hello World:"))

for i in range(1,User + 1):
    print("Hello world")

    


