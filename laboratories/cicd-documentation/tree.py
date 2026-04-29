from typing import Optional

from node import Node


class Tree:
    """Represent a binary search tree."""

    def __init__(self) -> None:
        """Initialize an empty tree."""
        self.root: Optional[Node] = None

    def getRoot(self) -> Optional[Node]:
        """Return the root node of the tree."""
        return self.root

    def add(self, data: int) -> None:
        """Insert a value into the tree."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data: int, node: Node) -> None:
        """Insert a value into the subtree rooted at ``node``.

        Args:
            data (int): Value to insert.
            node (Node): Root of the subtree where the value is inserted.
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data: int) -> Optional[Node]:
        """Find a value in the tree.

        Args:
            data (int): Value to search for.

        Returns:
            Optional[Node]: Matching node if the value exists, otherwise ``None``.
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data: int, node: Node) -> Optional[Node]:
        """Search for a value inside the subtree rooted at ``node``.

        Args:
            data (int): Value to search for.
            node (Node): Current subtree root used during recursion.

        Returns:
            Optional[Node]: Matching node if found, otherwise ``None``.
        """
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)
        return None

    def deleteTree(self) -> None:
        """Remove all nodes from the tree."""
        self.root = None

    def printTree(self) -> None:
        """Print the tree using in-order traversal."""
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node: Optional[Node]) -> None:
        """Print the subtree rooted at ``node`` in in-order."""
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node: Optional[Node]) -> None:
        """Print the subtree rooted at ``node`` in pre-order."""
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node: Optional[Node]) -> None:
        """Print the subtree rooted at ``node`` in post-order."""
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')
