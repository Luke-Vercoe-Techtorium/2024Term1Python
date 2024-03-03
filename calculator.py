def input_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def input_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")

def calculator() -> None:
    a = input_number("Enter the first number: ")
    b = input_number("Enter the second number: ")
    while True:
        op = input("Enter the operation (+, -, *, /): ")
        op = op.strip()
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            try:
                result = a / b
            except ZeroDivisionError:
                result = float("nan")
        else:
            print("Please enter a valid operation")
            continue
        break
    print(f"{a} {op} {b} = {result}")

def even_or_odd() -> None:
    value = input_integer("Enter a value: ")
    if value % 2 == 0:
        print(f"{value} is even")
    else:
        print(f"{value} is odd")

def ask_age() -> None:
    age = input_number("Enter your age: ")
    if age >= 18:
        print("You are elegible to vote")
    else:
        print("You are not elegible to vote")

# 5 * 2 + 3
# * is done before +
# so its (5 * 2) + 3 = 10 + 3 = 13

def name() -> None:
    name = input("What is your name? ")
    print(f"Hello, {name}!")

def add() -> None:
    a = input_number("Enter the first number: ")
    b = input_number("Enter the second number: ")
    print(f"{a} + {b} = {a + b}")

def color() -> None:
    color = input("What is your favourite color? ")
    print(f"{color} is a nice color!")

def multiple_lines() -> None:
    print("Line 1")
    print("Line 2")

def repeated() -> None:
    for _ in range(5):
        print("Hello")

def swap() -> None:
    x = 5
    y = 10
    print(f"x = {x}, y = {y}")
    x, y = y, x
    print(f"x = {x}, y = {y}")

def concatenation() -> None:
    a = "Hello, "
    b = "World"
    print(a + b)

def initialization() -> None:
    age = 18

def operators() -> None:
    a = input_number("Enter the first number: ")
    b = input_number("Enter the second number: ")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

def comparison() -> None:
    a = input_number("Enter the first number: ")
    b = input_number("Enter the second number: ")
    if a == b:
        print("The numbers are equal")
    else:
        print("The numbers are not equal")

def positive_or_negative() -> None:
    value = input_number("Enter a number: ")
    if value > 0:
        print(f"{value} is positive")
    elif value < 0:
        print(f"{value} is negative")
    else:
        print(f"{value} is zero")

def loop() -> None:
    for i in range(10):
        print(f"{i + 1}")
