import unittest

from node import Node
from tree import Tree


class TestTreeFind(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Tree()
        for value in [5, 3, 8, 1, 4, 7, 9, 0, 2, 6]:
            self.tree.add(value)

    def root(self) -> Node:
        root = self.tree.root
        assert root is not None
        return root

    def assertFindsValue(self, value: int) -> Node:
        node = self.tree.find(value)

        assert node is not None
        self.assertEqual(value, node.data)
        return node

    def test_find_returns_none_for_empty_tree(self) -> None:
        empty_tree = Tree()

        self.assertIsNone(empty_tree.find(5))

    def test_find_returns_root_node_when_value_is_root(self) -> None:
        node = self.tree.find(5)

        assert node is not None
        self.assertIs(node, self.root())
        self.assertEqual(5, node.data)

    def test_find_returns_existing_values_from_all_tree_levels(self) -> None:
        for value in [5, 3, 8, 1, 4, 7, 9, 0, 2, 6]:
            with self.subTest(value=value):
                self.assertFindsValue(value)

    def test_find_returns_nodes_from_left_and_right_subtrees(self) -> None:
        left_node = self.tree.find(3)
        right_node = self.tree.find(8)
        root = self.root()

        self.assertIs(left_node, root.left)
        self.assertIs(right_node, root.right)

    def test_find_returns_none_when_value_does_not_exist_between_nodes(self) -> None:
        node = self.tree.find(10)

        self.assertIsNone(node)

    def test_find_returns_none_when_value_is_below_minimum(self) -> None:
        node = self.tree.find(-1)

        self.assertIsNone(node)

    def test_find_returns_none_when_value_is_above_maximum(self) -> None:
        node = self.tree.find(12)

        self.assertIsNone(node)

    def test_private_find_returns_node_when_value_exists(self) -> None:
        node = self.tree._find(2, self.root())

        assert node is not None
        self.assertEqual(2, node.data)

    def test_private_find_returns_none_when_value_does_not_exist(self) -> None:
        node = self.tree._find(11, self.root())

        self.assertIsNone(node)


if __name__ == '__main__':
    unittest.main()
