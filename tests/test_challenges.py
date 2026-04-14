"""Weekly Coding #5 starter code: Trees, traversals, and BST basics."""

from __future__ import annotations

from typing import Any


class TreeNode:
    """A simple binary tree node."""

    def __init__(
        self,
        value: Any,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def preorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in preorder: node, left, right."""
    if root is None:
        return []
    return [root.value] + preorder_values(root.left) + preorder_values(root.right)


def inorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in inorder: left, node, right."""
    if root is None:
        return []
    return inorder_values(root.left) + [root.value] + inorder_values(root.right)


def postorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in postorder: left, right, node."""
    if root is None:
        return []
    return postorder_values(root.left) + postorder_values(root.right) + [root.value]


def bst_contains(root: TreeNode | None, target: int) -> bool:
    """Return True if target exists in the BST. Otherwise return False."""
    if root is None:
        return False
    if target == root.value:
        return True
    if target < root.value:
        return bst_contains(root.left, target)
    return bst_contains(root.right, target)


def bst_insert(root: TreeNode | None, value: int) -> TreeNode:
    """Insert value into the BST and return the root node.

    Duplicate values should be ignored.
    """
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = bst_insert(root.left, value)
    elif value > root.value:
        root.right = bst_insert(root.right, value)
    # value == root.value → duplicate, do nothing
    return root