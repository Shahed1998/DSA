# Blind 75 — Progress & Revisit Tracker

## How I'm using this list

**Pass 1 (in progress):** Solve every problem, however I can get there. Priority is completion and exposure, not elegance.

**Pass 2 (revisit):** For each problem —
1. Attempt cold, no notes, ~20–25 min timer for mediums.
2. Solved it? → Compare against the optimal approach/complexity anyway.
3. Stuck? → Look at just the *pattern* (one line, no code), try again from that hint.
4. Still stuck? → Read the full solution, understand it, re-solve it fresh the next day.
5. Space revisits out by a few days — recognition right after solving doesn't test retention.

**Status key:** ⬜ not started · 🟡 pass 1 done · 🟢 pass 2 done (cold) · 🔵 pass 2 done (needed hint/solution)

---

## Arrays & Hashing

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Two Sum | Hashmap lookup | |
| ⬜ | Contains Duplicate | Hashset | |
| ⬜ | Valid Anagram | Char frequency count | |
| ⬜ | Group Anagrams | Hashmap with sorted-string key | |
| ⬜ | Top K Frequent Elements | Heap / bucket sort | |
| ⬜ | Product of Array Except Self | Prefix/suffix products | |
| ⬜ | Valid Sudoku | Hashset per row/col/box | |
| ⬜ | Encode and Decode Strings | Length-prefix encoding | |
| ⬜ | Longest Consecutive Sequence | Hashset, check sequence starts | |

## Two Pointers

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Valid Palindrome | Two pointers converging | |
| ⬜ | 3Sum | Sort + two pointers | |
| ⬜ | Container With Most Water | Two pointers, move shorter side | |

## Sliding Window

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Best Time to Buy and Sell Stock | Track min so far | |
| ⬜ | Longest Substring Without Repeating Characters | Sliding window + hashset | |
| ⬜ | Longest Repeating Character Replacement | Sliding window + max freq char | |
| ⬜ | Minimum Window Substring | Sliding window + char count map | |

## Stack

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Valid Parentheses | Stack matching | |

## Binary Search

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Find Minimum in Rotated Sorted Array | Modified binary search | |
| ⬜ | Search in Rotated Sorted Array | Modified binary search | |

## Linked List

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| 🟢 | Reverse Linked List | Iterative pointer reversal | |
| ⬜ | Merge Two Sorted Lists | Dummy head + two pointers | |
| ⬜ | Reorder List | Find middle + reverse half + merge | Same building blocks as twin sum |
| 🟢 | Remove Nth Node From End of List | Fast/slow with gap | |
| ⬜ | Linked List Cycle | Fast/slow (Floyd's) | |
| ⬜ | Merge k Sorted Lists | Heap or divide & conquer | |
| 🟢 | Delete the Middle Node of a Linked List | Fast/slow two-pointer | Solved with hint |
| 🟢 | Maximum Twin Sum of a Linked List | Find middle + reverse half + walk together | Optimal O(1) space version done |

## Trees

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Invert Binary Tree | DFS/BFS swap children | |
| ⬜ | Maximum Depth of Binary Tree | DFS recursion | |
| ⬜ | Same Tree | DFS comparison | |
| ⬜ | Subtree of Another Tree | DFS + same-tree check | |
| ⬜ | Lowest Common Ancestor of a BST | BST property traversal | |
| ⬜ | Binary Tree Level Order Traversal | BFS with queue | |
| ⬜ | Validate Binary Search Tree | DFS with min/max bounds | |
| ⬜ | Kth Smallest Element in a BST | Inorder traversal | |
| ⬜ | Construct Binary Tree from Preorder and Inorder Traversal | Recursion + index map | |
| ⬜ | Binary Tree Maximum Path Sum | DFS returning max branch | |
| ⬜ | Serialize and Deserialize Binary Tree | Preorder DFS with markers | |

## Heap / Priority Queue

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Find Median from Data Stream | Two heaps | |

## Backtracking

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Combination Sum | Backtracking with pruning | |
| ⬜ | Word Search | Backtracking DFS on grid | |

## Tries

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Implement Trie (Prefix Tree) | Trie node structure | |
| ⬜ | Design Add and Search Words Data Structure | Trie + DFS for wildcards | |
| ⬜ | Word Search II | Trie + backtracking on grid | |

## Graphs

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Number of Islands | DFS/BFS flood fill | |
| ⬜ | Clone Graph | DFS/BFS + hashmap of visited | |
| ⬜ | Pacific Atlantic Water Flow | Multi-source DFS/BFS | |
| ⬜ | Course Schedule | Topological sort / cycle detection | |
| ⬜ | Graph Valid Tree | Union-Find or DFS cycle check | |
| ⬜ | Number of Connected Components in an Undirected Graph | Union-Find | |

## Advanced Graphs

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Alien Dictionary | Topological sort from constraints | |

## 1-D Dynamic Programming

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Climbing Stairs | Fibonacci-style DP | |
| ⬜ | House Robber | DP, skip-adjacent | |
| ⬜ | House Robber II | DP on circular array (two passes) | |
| ⬜ | Longest Palindromic Substring | Expand around center | |
| ⬜ | Palindromic Substrings | Expand around center, count | |
| ⬜ | Decode Ways | DP counting valid splits | |
| ⬜ | Coin Change | DP, min coins for amount | |
| ⬜ | Maximum Product Subarray | Track running max & min | |
| ⬜ | Word Break | DP with substring check | |
| ⬜ | Longest Increasing Subsequence | DP or patience sorting | |

## 2-D Dynamic Programming

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Unique Paths | Grid DP | |
| ⬜ | Longest Common Subsequence | 2D DP table | |

## Greedy

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Maximum Subarray | Kadane's algorithm | |
| ⬜ | Jump Game | Greedy reachability | |

## Intervals

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Insert Interval | Merge while scanning sorted intervals | |
| ⬜ | Merge Intervals | Sort + merge overlapping | |
| ⬜ | Non-overlapping Intervals | Sort + greedy removal | |
| ⬜ | Meeting Rooms | Sort + overlap check | |
| ⬜ | Meeting Rooms II | Min-heap of end times | |

## Math & Bit Manipulation

| Status | Problem | Pattern | Notes |
|---|---|---|---|
| ⬜ | Sum of Two Integers | Bitwise add (XOR + carry) | |
| ⬜ | Number of 1 Bits | Bit counting | |
| ⬜ | Counting Bits | DP over bit patterns | |
| ⬜ | Missing Number | XOR or sum formula | |
| ⬜ | Reverse Bits | Bitwise manipulation | |

---

## Pattern index (fill in as you go)

Keep a running note of which pattern each problem belongs to, in your own words — this ends up more valuable than the 75 solutions themselves, since new problems are usually variations on a pattern rather than repeats.

- **Fast/slow pointers:** find middle, detect cycle, remove nth-from-end
- **Reverse + merge:** reorder list, twin sum — reversal turns "look up the twin" into "walk two pointers together"
- *(add more as you notice them)*

## Mistakes log

Quick log of bugs that bit you more than once, so you stop re-making them:
- *(e.g. off-by-one in `range()`, forgetting to update pointer before overwriting `.next`, float vs int division)*
