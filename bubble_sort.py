def bubble_sort(x: list[int]) -> None:
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(x)):
            if x[i - 1] > x[i]:
                x[i], x[i - 1] = x[i - 1], x[i]
                sorted = False

def insertion_sort(x: list[int]) -> None:
    for i in range(1, len(x)):
        while i > 0 and x[i - 1] > x[i]:
            x[i - 1], x[i] = x[i], x[i - 1]
            i -= 1

x = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
bubble_sort(x)
print(x)

y = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
insertion_sort(y)
print(y)
