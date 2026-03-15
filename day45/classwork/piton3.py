#3) დაწერე ფუნქცია რომელიც პარამეტრად მიიღებს მომხმარებლის დაბადების წელს და გამოთვლის რამდენი წლისაა ის დღეს

def Birth_year(year):
    current_year = 2026
    age = current_year - year
    return age


print(Birth_year(2007))