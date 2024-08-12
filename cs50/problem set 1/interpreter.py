Expression = input("Expression: " )
x, y, z = Expression.split(" ")
num1 , num2 = float(x) , float(z)

if y == "+":
    print(num1+num2)
elif y == "-":
    print(num1-num2)
elif y == "*":
    print(num1*num2)
elif y == "/":
    print(num1/num2)


