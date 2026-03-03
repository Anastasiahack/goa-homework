# დავალება 1

# შედარების ოპერატორები
#== _ 
#!=
#>
#<
#>=
#<=

# ლოგიკური ოპერატორები
#and
#or
#not

# დავალება 2

number=int(input("შეიყვანეთ რიცხვი"))
Even_Odd=number % 2==0
print("ლუწია თუ კენტია ?", Even_Odd) # True თუ ლუწია, False თუ კენტია


# დავალება 3

# 1 სენახული ლოგინი და პაროლი
saved_login="Snake"
saved_password="678976"

# 2 მომხმარებლის მიერ შეყვანილი ლოგინი და პაროლი
userd_login=input("შეიყვანეთ ლოგინი: ")
user_password=input("შეიყვანეთ პაროლი: ")

# 3 შედარება

is_authenticated=user_login==saved_login and user_password==saved_password 

# 4. შედეგის დაბეჭვდა
print("შესვლის სტატუსი:", is_authenticated) # True თუ სწორი , False თუ მცდარია 













