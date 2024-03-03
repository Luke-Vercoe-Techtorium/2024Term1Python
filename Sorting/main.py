from typing import MutableSequence, Sequence, Protocol, TypeVar
import pandas as pd

class _Comparable(Protocol):
    this = TypeVar('this')
    def __lt__(self: this, other: this) -> bool: ...
    def __gt__(self: this, other: this) -> bool: ...
Comparable = TypeVar('Comparable', bound=_Comparable)

def bubble_sort(x: MutableSequence[Comparable]) -> None:
    sorted = False
    for _ in range(0, len(x) - 1):
        sorted = True
        for i in range(1, len(x)):
            if x[i - 1] > x[i]:
                x[i - 1], x[i] = x[i], x[i - 1]
                sorted = False
        if sorted:
            return
    assert False, "unreachable"

def insertion_sort(x: MutableSequence[Comparable]) -> None:
    for i in range(1, len(x)):
        while i > 0 and x[i - 1] > x[i]:
            x[i - 1], x[i] = x[i], x[i - 1]
            i -= 1

def selection_sort(x: MutableSequence[Comparable]) -> None:
    for i in range(0, len(x)):
        smallest = -1
        for j in range(i, len(x)):
            if smallest == -1 or x[j] < x[smallest]:
                smallest = j
        assert smallest != -1, "there should be a smallest"
        x[i], x[smallest] = x[smallest], x[i]

def merge_sort(x: Sequence[Comparable]) -> list[Comparable]:
    if len(x) == 0:
        return []
    elif len(x) == 1:
        return [x[0]]
    else:
        middle = len(x) // 2
        left = merge_sort(x[:middle])
        right = merge_sort(x[middle:])

        left_index = 0
        right_index = 0
        result: list[Comparable] = []
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

def quick_sort(x: MutableSequence[Comparable]) -> None:
    def quick_sort(x: MutableSequence[Comparable], lo: int, hi: int) -> None:
        if lo >= hi or lo < 0:
            return

        p = partition(x, lo, hi)

        quick_sort(x, lo, p - 1)
        quick_sort(x, p + 1, hi)

    def partition(x: MutableSequence[Comparable], lo: int, hi: int) -> int:
        pivot = x[hi]
        i = lo
        for j in range(lo, hi):
            if x[j] < pivot:
                x[j], x[i] = x[i], x[j]
                i += 1
        x[hi], x[i] = x[i], x[hi]
        return i

    quick_sort(x, 0, len(x) - 1)

def main() -> None:
    weights: list[float] = pd.read_csv("C:\\Users\\lukev\\Downloads\\kiwi_data.csv")["Weight(kg)"].tolist()
    quick_sort(weights)
    print(weights)

if __name__ == "__main__":
    main()
