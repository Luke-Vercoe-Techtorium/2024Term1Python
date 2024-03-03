from typing import *

def input_integer(question: str) -> int:
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Please enter a valid integer")

def main():
    value = input_integer("Please enter an integer: ")
    if value % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

if __name__ == "__main__":
    main()
