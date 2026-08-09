#1 მოცემულია სტრინგ "python" გაზარდე სტრინგის მხოლოდ პირველი ასო

Variable1="python"

value1=Variable1.capitalize()

print(value1)


#2 მოცემულია სტრინგი "PYTHON is great" დააპატარავე სტრინგში ყველა ასო

Variable2="PYTHON is great"

value2=Variable2.casefold()

print(value2)


#3 მოცემულია სტრინგი "python is great" შეამოწმე მთავრდება თუ არა სტრინგი სიტყვა is ით

Variable3="python is great" 

value3=Variable2.endswith("is")

print(value3)


#4 მოცემულია სტრინგი "python is great" დაითვალე რამდენჯერ მეორდება ასო t სტრინგში

Variable4="python is great"

value4=Variable4.count("t")

print(value4)


#5 მოცემულაი სტრინგ "python is great" იპოვეთ is ის ინდექსი, თუ სიტყვა არ არსებობს დააბრუნოს ერორი

Variable5="python is great"

value5=Variable5.index("is")

print(value5)



#6 მოცემულია სტრინგი "python is great" იპოვეთ nika ს ინდექსი, თუ სიტყვა არ არსებობს დააბრუნოს -1

Variable6="python is great"

value6=Variable6.index("is")

print(value6)


#7 მოცემულია სტრინგი "python is great" შეამოწმე სტრინგში ყველა ნიშანი არის თუ არა რიცხვი

Variable7="python is great"

value7=Variable7.find("nika")

print(value7)


#8 მოცემულია სტრინგი "python#is#great" დაშალე სტრინგი #-ზე ისე რომ შეიქმნას სია და მასში შეინახოს თითოეული სიტყვა

Variable8="python#is#great"

value8=Variable8.split("#")

print(value8)



#9 მოცემულია სია ["python", "is", "great"] გააერთიანე სია ერთ სტრინგად, თითოეული ელემენტი გამოყავი - ით

Variable9=["python", "is", "great"]

value9="-".join(Variable9)

print(value9)


#10 მოცემულია სტრინგი "Mercedes is the fastest car" fastest ჩაანაცვლე slowest ით

Variable10="Mercedes is the fastest car"

value10=Variable10.replace("fastest", "slowest")

print(value10)


































