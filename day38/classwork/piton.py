points = 70      
wins = 3         

rule = "points >= 60 and wins >= 2"  
next_level = eval(rule)  

print("შემდეგ ეტაპზე გადავიდა?", next_level)


