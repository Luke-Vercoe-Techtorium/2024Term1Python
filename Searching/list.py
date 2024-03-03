from typing import TypeVar, Sequence, Protocol
from typing_extensions import Self

# create a general type variable, any python value can be compared for equality
T = TypeVar('T')

def linear_search(xs: Sequence[T], value: T) -> tuple[int, T] | None:
    for (i, x) in enumerate(xs):
        if x == value:
            return (i, x)
    return None

# create a type variable that ensures the elements can be ordered
class Comparible(Protocol):
    def __lt__(self, rhs: Self) -> bool: ...
C = TypeVar('C', bound=Comparible)

def is_sorted(xs: Sequence[C]) -> bool:
    for i in range(1, len(xs)):
        if xs[i - 1] > xs[i]:
            # if any element is greater than its predecessor then the list is not sorted
            return False
    return True

def binary_search(xs: Sequence[C], value: C) -> tuple[int, C] | None:
    assert is_sorted(xs)

    # the range [low, high) where the element might be
    low = 0
    high = len(xs)

    # if low == high then either nothing was found, or the list is empty
    while low != high:
        middle = low + (high - low) // 2

        if xs[middle] < value:
            # move to the upper half
            # + 1 to skip the middle element
            low = middle + 1
        elif xs[middle] > value:
            # move to the lower half
            # high is already excluded, so no need to explicitly skip the middle element
            high = middle
        elif xs[middle] == value:
            # found the value
            return (middle, xs[middle])
        else:
            # value is not less, greater, or equal to the middle element, something is wrong so
            # we just `return None` to avoid an infinite loop
            return None

    # found nothing
    return None

def main() -> None:
    print(linear_search([], 10))
    print(linear_search([1, 2, 3, 4, 5, 10], 7))
    print(linear_search([1, 2, 3, 4, 5, 10], 4))
    print(linear_search([1, 2, 3, 4, 5, 10], 3))

    print(binary_search([], 10))
    print(binary_search([1, 2, 3, 4, 5, 10], 7))
    print(binary_search([1, 2, 3, 4, 5, 10], 4))
    print(binary_search([1, 2, 3, 4, 5, 10], 3))

if __name__ == "__main__":
    main()
