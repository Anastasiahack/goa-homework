#3)მომხმარებელს შემოატანინეთ რიცხვი მანამ სანამ ესრიცხვი არ იქნება ლუწი,
#  ხოლო როდესაც მომხმარებელი შეიყვანს ლუწ რიცხვს ,
#  ტერმინალში დაიპრინტოს "You enter an even number and the loop is over"

num = int(input("შეიყვანე რიცხვი: "))
while num % 2 != 0:
    num = int(input("შეიყვანე რიცხვი: "))

print("You enter an even number and the loop is over")