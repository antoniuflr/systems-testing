from typing import Optional


class Node:
    """ Node class for binary tree """

    def __init__(self, data: int) -> None:
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.data = data
