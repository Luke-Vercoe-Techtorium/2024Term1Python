shopping_list: list[str] = []
shopping_list.append("apple")
shopping_list.append("banana")
shopping_list.append("orange")
print(shopping_list)

shopping_list.append("grapes")
shopping_list.remove("banana")
print(shopping_list)

coordinates = (1, 2)

a: set[int] = {0, 1, 2, 3}
b: set[int] = {2, 6, 4, 5}
print(a.union(b))
