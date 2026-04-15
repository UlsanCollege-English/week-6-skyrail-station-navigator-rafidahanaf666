"""Public tests for Weekly Coding #5."""

from __future__ import annotations

from src.challenges import (
    TreeNode,
    bst_contains,
    bst_insert,
    inorder_values,
    postorder_values,
    preorder_values,
)


def build_station_map_tree() -> TreeNode:
    """Build the sample Skyrail station map tree used in traversal tests."""
    return TreeNode(
        "Central",
        TreeNode("North Line", TreeNode("Maple"), TreeNode("Elm")),
        TreeNode("South Line", None, TreeNode("Harbor")),
    )


def build_single_station_tree() -> TreeNode:
    """Build a one-node tree for traversal edge-case tests."""
    return TreeNode("Central")


def build_station_bst() -> TreeNode:
    """Build the sample BST used in search and insert tests."""
    return TreeNode(
        40,
        TreeNode(20, TreeNode(10), TreeNode(30)),
        TreeNode(60, TreeNode(50), TreeNode(70)),
    )


def test_preorder_values_returns_expected_order_for_sample_tree() -> None:
    root = build_station_map_tree()
    assert preorder_values(root) == [
        "Central",
        "North Line",
        "Maple",
        "Elm",
        "South Line",
        "Harbor",
    ]


def test_inorder_values_returns_expected_order_for_sample_tree() -> None:
    root = build_station_map_tree()
    assert inorder_values(root) == [
        "Maple",
        "North Line",
        "Elm",
        "Central",
        "South Line",
        "Harbor",
    ]


def test_postorder_values_returns_expected_order_for_sample_tree() -> None:
    root = build_station_map_tree()
    assert postorder_values(root) == [
        "Maple",
        "Elm",
        "North Line",
        "Harbor",
        "South Line",
        "Central",
    ]


def test_traversals_return_empty_list_for_empty_tree() -> None:
    assert preorder_values(None) == []
    assert inorder_values(None) == []
    assert postorder_values(None) == []


def test_traversals_work_for_single_node_tree() -> None:
    root = build_single_station_tree()
    assert preorder_values(root) == ["Central"]
    assert inorder_values(root) == ["Central"]
    assert postorder_values(root) == ["Central"]


def test_traversals_work_for_left_heavy_tree() -> None:
    root = TreeNode("C", TreeNode("B", TreeNode("A")), None)
    assert preorder_values(root) == ["C", "B", "A"]
    assert inorder_values(root) == ["A", "B", "C"]
    assert postorder_values(root) == ["A", "B", "C"]


def test_bst_contains_returns_true_for_existing_values() -> None:
    root = build_station_bst()
    assert bst_contains(root, 40) is True
    assert bst_contains(root, 10) is True
    assert bst_contains(root, 50) is True
    assert bst_contains(root, 70) is True


def test_bst_contains_returns_false_for_missing_values() -> None:
    root = build_station_bst()
    assert bst_contains(root, 25) is False
    assert bst_contains(root, 65) is False
    assert bst_contains(root, 99) is False


def test_bst_contains_returns_false_for_empty_tree() -> None:
    assert bst_contains(None, 123) is False


def test_bst_insert_creates_root_when_tree_is_empty() -> None:
    root = bst_insert(None, 40)
    assert root.value == 40
    assert root.left is None
    assert root.right is None


def test_bst_insert_adds_value_to_left_subtree() -> None:
    root = build_station_bst()
    updated = bst_insert(root, 25)
    assert inorder_values(updated) == [10, 20, 25, 30, 40, 50, 60, 70]


def test_bst_insert_adds_value_to_right_subtree() -> None:
    root = build_station_bst()
    updated = bst_insert(root, 65)
    assert inorder_values(updated) == [10, 20, 30, 40, 50, 60, 65, 70]


def test_bst_insert_adds_deeper_leaf_in_correct_position() -> None:
    root = build_station_bst()
    updated = bst_insert(root, 55)
    assert inorder_values(updated) == [10, 20, 30, 40, 50, 55, 60, 70]
    assert bst_contains(updated, 55) is True


def test_bst_insert_ignores_duplicate_values() -> None:
    root = build_station_bst()
    updated = bst_insert(root, 60)
    assert inorder_values(updated) == [10, 20, 30, 40, 50, 60, 70]


def test_bst_insert_can_build_a_tree_from_scratch() -> None:
    root = None
    for value in [40, 20, 60, 10, 30, 50, 70]:
        root = bst_insert(root, value)

    assert root is not None
    assert inorder_values(root) == [10, 20, 30, 40, 50, 60, 70]
    assert preorder_values(root) == [40, 20, 10, 30, 60, 50, 70]