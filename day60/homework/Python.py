# 1 append()შექმენი ცარიელი სია და დაამატე მასში რიცხვები: 10, 20, 30.

Tens=[60, 50, 40,]

Tens.append(10)

Tens.append(20)

Tens.append(30)

print(Tens)




# 2 extend()
#   გაქვს:
#   a = [1, 2, 3]
#   b = [4, 5, 6]
#   გააერთიანე b სია a-სთან extend()-ის გამოყენებით.

a = [1, 2, 3]

b = [4, 5, 6]

b.extend(a)

print(b)


# 3 insert()
#   გაქვს:
#   names = ["Nika", "Gio", "Luka"]
#   ჩასვი "Saba" მეორე პოზიციაზე.


names = ["Nika", "Gio", "Luka"]

names.insert(1, "Saba")

print(names)



# 4 remove()
#   გაქვს:
#   colors = ["red", "blue", "green", "blue"]
#   წაშალე მხოლოდ პირველი "blue".

colors = ["red", "blue", "green", "blue"]

colors.remove("blue")

print(colors)




# 5 pop()
#   გაქვს:
#   numbers = [5, 10, 15, 20]
#   წაშალე ბოლო ელემენტი და შეინახე ცვლადში.


numbers = [5, 10, 15, 20]

result=numbers.pop(-1)

print(result)


# 6 letters = ["a", "b", "c", "d"]
#   წაშალე "b" ინდექსის გამოყენებით.

letters = ["a", "b", "c", "d"]

letters.pop(1)

print(letters)



# 7 index()
#   იპოვე "banana"-ს ინდექსი.
#   fruits = ["apple", "banana", "orange", "kiwi"]


fruits = ["apple", "banana", "orange", "kiwi"]

print(fruits.index("banana"))



# 8 დათვალე რამდენჯერ გვხვდება 5.
#   nums = [5, 2, 5, 7, 5, 1]


nums = [5, 2, 5, 7, 5, 1]

print(nums.count(5))



# 9 დაალაგე ზრდადობით.
#   nums = [8, 2, 10, 1, 6]


nums = [8, 2, 10, 1, 6]

nums.sort()

print(nums)



# 10 იგივე სია დაალაგე კლებადობით.


nums = [8, 2, 10, 1, 6]

nums.sort(reverse=True)

print(nums)



# 11 numbers = [1, 2, 3, 4, 5]
#    შეაბრუნე სია.

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)



# 12 შექმენი სიის ასლი და დაამატე ახალ სიაში 100.
#    დარწმუნდი, რომ ორიგინალი არ შეიცვალა.
#    რთული


numbers=[666, 777, 888, 999]

result_num=numbers.copy()

numbers.append(100)

print(result_num, numbers)




# 13 შექმენი ახალი სია, სადაც ჩაიწერება მხოლოდ ლუწი რიცხვები.
#    nums = [3, 6, 9, 10, 15, 18]


nums = [3, 6, 9, 10, 15, 18]

result=[]

for i in nums:

    if i % 2 == 0:
        
        result.append(i)

        print(result)




# 14 წაშალე სიიდან ყველა 0.
#    nums = [0, 3, 0, 5, 0, 7, 8]
#    (მინიშნება: გამოიყენე while.)


nums= [0, 3, 6, 0, 5, 0, 7, 9, 8, 0]


while 0 in nums:
    nums.remove(0)

print(nums)



# 15 დაწერე პროგრამა, რომელიც იტყვის, არის თუ არა სიაში 7 მინიმუმ 3-ჯერ.


def seven(num):
    counted=num.count(7)

    if counted == 3:
        return True
    else:
        return False

integers=[1,7,8,7,9,7]
print(seven(integers))



# 16 იპოვე "Python"-ის ინდექსი მხოლოდ იმ შემთხვევაში, თუ არსებობს სიაში.

string=["JavaScript", "Java", "Python", "HTML", "CSS",]

if "Python" in string:
    print(string.index("Python"))
else:
    print(None)    



# 17 მომხმარებლის მიერ შექმნილი სია მთლიანად გაასუფთავე.

user=input("Text:")

value_list=user.split(",")

value_list.clear()

print(value_list)



# 18 გაქვს სამი სია:
#    a = [1, 2]
#    b = [3, 4]
#    c = [5, 6]
#    გააერთიანე ყველა ერთ სიაში მხოლოდ extend()-ის გამოყენებით.


a = [1, 2]
b = [3, 4]
c = [5, 6]

result=[]

a.extend(b)

a.extend(c)

print(a)


#19 კომბინირებული
#   გაქვს:
#   nums = [7, 3, 8, 1, 5]
#   გააკეთე შემდეგი:
#   დაამატე 10
#   წაშალე 3
#   დაალაგე
#   შეაბრუნე
#   დაბეჭდე საბოლოო სია


nums = [7, 3, 8, 1, 5]

nums.append(10)

nums.remove(3)

nums.sort()

nums.reverse()

print(nums)



































