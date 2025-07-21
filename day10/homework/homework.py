#დავალება 1

#Data convertion-მონაცემთა ტიპის შეცვლა კონვერტაცია-ამისთვის ვიყენებთ ამ ფუნქციებს როგორიცაა:
int() # გარდაქმნის მონაცემებს ყველა მთელ რიცხვად,
float() # გარდაქმნის მონაცემებს ყველა ათწილადად,
str() # გარდაქმნის მონაცემებს ყველა სტრინგად,
bool() # გარდაქმნის მონაცემებს ყველა True და False -ად.

#დავალება 2

#Explicit Type conversion-მონაცემის ტიპის შეცვალ, ხილულად int(), float(), str(), bool(), ფუნქციების გამოყენებით. 

# Implicit Type Conversion-მონაცემის ტიპის შეცვლა, ფარულად, ჩაშენებული ფუნქციების გამოყენების გარეშე. 

#დავალება 3
Fruit="Coconut"
coconut=100
Palmtree=66.6
Mint=True
Chamomile=False

print(bool(Fruit))
print(float(coconut))
print(str(Palmtree))
print(bool(Mint))
print(str(Chamomile))

# დავალება 4

# მაგალითი - 1
C=100
A=777
result=C*A
print(result)

# მაგალითი - 2
x=999
y=666
result=999/666
print(result)

# მაგალითი - 3
cocnut=False
Chamomile=666
result=coconut+Chamomile
print(result)

# დავალება 5
# concatenation-კონკატენაცია არის მონაცემთა ტიპების შეერთება. 

# მაგალითი - 1
a="helow"
b="world"
print(a + " " + b )

# მაგალითი - 2


# მაგალითი - 3
fruit="strawberry"
Piese=100
print(fruit + " " + str(Piese)+ " " +"Piese")

# მაგალითი - 4

Fat="butter"
insect="fly"
print(Fat+insect)

# დავალება 6

birzth_yer=int(input("შეიყვანეთ თქვენი დაბადების წელი : "))

# მიმდინარე წლის მიღება 
current_year=int(input("შეიყვანეთ თქვენი მიმდინარე წელი : "))

#ასაკის გამოთვლა

age=current_year - birzth_yer

# შედეგის გამოტანა

print( "თქვენ ხართ" , age, "წლის" )

# დავალება 7
 
name="snake"
surname="..."
age=999
height=1.99
address="საქართველო"
address2=address+"ში"

print("მე ვარ" + " " + name + " " + surname + " " + ",ასაკი მაქვს " + str(age) + " წელი, სიმაღლე " + str(height) + " მეტრი და ვცხოვრობ " + 
address2 + " . " )



