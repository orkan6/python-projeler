camel = input("camelCase: ")
print("snake_case: ", end="")

snake_case = ""

for i in camel:
    if i.isupper():
        snake_case += "_" + i.lower()
    else:
        snake_case += i

print(snake_case)
