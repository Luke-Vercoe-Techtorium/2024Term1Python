from typing import *

class Vendor:
    def __init__(self, phone: str, email: str) -> None:
        self.phone = phone
        self.email = email

def input_string(prompt: str) -> str:
    while True:
        line = input(prompt)
        line = line.strip()
        if len(line) != 0:
            return line
        print("Please enter something")

def input_vendor() -> Tuple[str, Vendor]:
    name = input_string("Enter the vendor name: ")
    phone = input_string("Enter the phone number: ")
    email = input_string("Enter the email address: ")
    return name.strip(), Vendor(phone.strip(), email.strip())

def main() -> None:
    vendors: dict[str, Vendor] = {}

    try:
        while True:
            command = input_string("Enter a command (use 'help' for a list of commands): ")
            if command == "help":
                print("Commands:")
                print("  help   - prints this message")
                print("  add    - allows you to add new vendor details")
                print("  search - allows you to search for vendor details")
                print("  remove - allows you to remove vendor details")
                print("  update - allows you to update vendor details")
            elif command == "add":
                name, vendor = input_vendor()
                if name in vendors:
                    print(f"A vendor named '{name}' already exists")
                else:
                    vendors[name] = vendor
            elif command == "search":
                name = input_string("Enter part of a vendor name to search for: ")
                found: list[str] = []
                for vendor_name in vendors:
                    if name in vendor_name:
                        found.extend(vendor_name)
                if len(found) == 0:
                    print(f"There were no matches for `{name}`")
                else:
                    print("Found vendors:")
                    for name in vendors:
                        print(f"  Vendor: {name}")
                        print(f"    Phone: {vendors[name].phone}")
                        print(f"    Email: {vendors[name].email}")
            elif command == "remove":
                name = input_string("Enter the vendor name: ")
                if name in vendors:
                    del vendors[name]
                else:
                    print(f"There is no vendor named '{name}'")
            elif command == "update":
                name, vendor = input_vendor()
                if name in vendors:
                    vendors[name] = vendor
                else:
                    print(f"There is no vendor named '{name}'")
            else:
                print("Unknown command, please try again")
            print()
    except KeyboardInterrupt:
        ...

if __name__ == "__main__":
    main()
