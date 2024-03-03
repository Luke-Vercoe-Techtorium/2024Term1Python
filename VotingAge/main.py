from typing import *

def input_number(question: str) -> float:
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("Please enter a valid number")

def main():
    age = input_number("Enter your age: ")
    if age >= 18:
        print("You are elegible to vote")
    else:
        print("You are not elegible to vote")

if __name__ == "__main__":
    main()
