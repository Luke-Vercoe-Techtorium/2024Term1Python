from typing import *

def input_number(question: str) -> float:
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("Please enter a valid number")

def main():
    a = input_number("Enter the first value: ")
    b = input_number("Enter the second value: ")
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
                result = "undefined"
        else:
            print("Please enter a valid operation")
            continue
        break
    print(f"{a} {op} {b} = {result}")

if __name__ == "__main__":
    main()
