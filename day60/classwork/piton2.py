num = [10, 20, 25, 29, 30, 48, 50]

num.append(120)

result = 0

for num in num:
    if num % 2 == 0:
        result += num

print(num)
print(result)