from typing import TypeVar, Generic
from typing_extensions import Self

T = TypeVar('T')

class BinaryTree(Generic[T]):
    def __init__(self, left: Self | None, right: Self | None, value: T) -> None:
        self.left = left
        self.right = right
        self.value = value

    def __eq__(self, other: object) -> bool:
        if super().__eq__(other):
            return True

        if isinstance(other, BinaryTree):
            return self.value == other.value and self.left == other.left and self.right == other.right
        else:
            return False

def bredth_first_search(root: BinaryTree[T], value: T) -> BinaryTree[T] | None:
    to_search = [root]
    while len(to_search) > 0:
        node = to_search.pop(0)
        if node.value == value:
            return node
        if node.left is not None:
            to_search.append(node.left)
        if node.right is not None:
            to_search.append(node.right)
    return None

def depth_first_search(root: BinaryTree[T], value: T) -> BinaryTree[T] | None:
    to_search = [root]
    while len(to_search) > 0:
        node = to_search.pop()
        if node.value == value:
            return node
        if node.right is not None:
            to_search.append(node.right)
        if node.left is not None:
            to_search.append(node.left)
    return None

def main() -> None:
    ...

if __name__ == "__main__":
    main()
