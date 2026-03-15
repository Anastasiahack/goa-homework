#2) დაწერე ფუნქცია max_number(a, b, c), რომელიც დააბრუნებს სამი რიცხვიდან ყველაზე დიდს.

def max_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print(max_number(7,6,3))   
