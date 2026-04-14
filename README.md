### `README.md`

```markdown
# Weekly Coding #5 — Skyrail Station Navigator

## Summary

This module implements core tree operations for the Skyrail Transit Team's
route-planning system. It supports three depth-first traversals (preorder,
inorder, postorder) on general binary trees, and provides BST-aware search
and insert functions for managing integer station IDs efficiently.

---

## Approach

- **Traversals** — each function uses a base case (`root is None → []`) and
  a recursive case that concatenates the current node's value with the results
  from the left and right subtrees, in the order required by the traversal type.
- **`bst_contains`** — exploits the BST invariant: go left if target is
  smaller, go right if larger, short-circuit on an exact match.
- **`bst_insert`** — follows the same left/right navigation until it reaches a
  `None` slot, places a new `TreeNode` there, and returns the (possibly new)
  root on the way back up. Duplicates are silently skipped.

---

## Complexity

### `preorder_values` / `inorder_values` / `postorder_values`
- **Time — O(n):** every node is visited exactly once regardless of tree shape.
- **Space — O(n):** the returned list holds all n values; the call stack depth
  is O(h) where h is the tree height (O(n) worst case for a skewed tree,
  O(log n) for a balanced one).

### `bst_contains`
- **Time — O(h):** at each node we eliminate one subtree, so we descend at
  most h levels. h = O(log n) for a balanced BST, O(n) for a degenerate
  (sorted-input) BST.
- **Space — O(h):** recursive call stack depth equals the height traversed.

### `bst_insert`
- **Time — O(h):** same navigation logic as `bst_contains`; we descend until
  we find the correct empty slot.
- **Space — O(h):** call stack depth equals the height of the path taken.

---

## Edge-case checklist

- [x] **Empty tree (`root is None`)** — all traversals return `[]`;
      `bst_contains` returns `False`; `bst_insert` creates and returns a
      brand-new root node.
- [x] **Single-node tree** — traversals return a one-element list; contains
      returns `True` or `False` correctly; insert on a matching value is a
      no-op.
- [x] **Missing target in BST** — `bst_contains` reaches a `None` leaf and
      returns `False` without raising an error.
- [x] **Duplicate insert value** — the `elif value > root.value` guard means
      equal values fall through to `return root` untouched; the tree is
      unchanged.

---

## Assistance & Sources

- **AI used:** No
- **Outside sources:** Course lecture slides on BST invariants; Python docs on
  type hints (`from __future__ import annotations`).
```