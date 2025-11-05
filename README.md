# Python DSA Repository

## Understanding Data Structures and Algorithms (DSA)

Data Structures and Algorithms (DSA) are the foundational pillars of computer science. They are the techniques used to organize data efficiently and to solve problems effectively within a program. Mastering DSA is crucial for writing optimized, scalable code and is a standard requirement for technical interviews at virtually all major software companies.

This repository offers beginner-friendly, fully documented Python implementations for a wide array of core DSA topics. Each solution aims to be clear and concise, making complex concepts easy to grasp.

---

## Data Structures

Data structures are specialized means of organizing and storing data in a computer so that it can be accessed and modified efficiently.

---

## Data Structures

| **Data Structure** | **Explanation** | **Unique Feature** |
|--------------------|-----------------|--------------------|
| **Lists and Arrays** | Sequential containers that store elements in contiguous memory locations. This allows for direct, immediate access to any element by its numerical index. | **Efficient indexing:** Accessing the 5th element is immediate (`my_list[4]`). |
| **Stacks** | A linear structure following the **LIFO** principle (Last-In, First-Out). The last item added is the first one removed. Think of a spring-loaded tray stack in a cafeteria. | **Strict operation:** Only two primary operations — `push` (add to the top) and `pop` (remove from the top). |
| **Queues** | A linear structure following the **FIFO** principle (First-In, First-Out). The first item added is the first one removed. Just like people waiting in a physical line. | **Ordered processing:** Ensures items are processed in the exact order they arrive. |
| **Linked Lists** | A sequence of individual nodes, where each node stores data and a reference (pointer) to the next node in the sequence. Unlike arrays, they don't require contiguous memory. | **Dynamic memory:** Highly efficient for insertions and deletions in the middle of the sequence without shifting elements. |
| **Hash Tables** | Stores data as key-value pairs. It uses a special function (a hash function) to quickly compute an index into an array of buckets or slots, where the corresponding value is stored. | **Constant-time lookups:** Provides an average time complexity of `O(1)` for both insertion and retrieval. |
| **Trees (Binary Trees, BSTs, AVL Trees)** | Hierarchical structures starting from a root node, which connects to child nodes. Binary Search Trees (BSTs) maintain a sorted order (`left child < parent < right child`) for efficient searching. AVL Trees are self-balancing BSTs that prevent worst-case scenarios by rotating nodes automatically. | **Hierarchical representation:** Ideal for modeling data with parent-child relationships and efficient search/sort operations. |
| **Graphs** | A collection of interconnected nodes (vertices) and links (edges). Graphs are incredibly versatile for modeling real-world networks like social media connections, road maps, or computer networks. | **Relationship modeling:** Highly flexible structure capable of representing complex network systems and optimizing paths between points. |

---

## Algorithms

Algorithms are well-defined, step-by-step procedures or formulas for solving a problem or achieving a specific outcome.

### Search Algorithms

| **Algorithm** | **Explanation** | **Unique Feature** |
|---------------|-----------------|--------------------|
| **Linear Search** | Checks every single element in a list sequentially until the target is found. | **Simplicity:** Works on unsorted lists but is slow (`O(n)`). |
| **Binary Search** | Finds an item in a sorted list by repeatedly dividing the search interval in half. | **Speed:** Incredibly fast (`O(log n)`) but requires sorted data. |

### Sorting Algorithms

| **Algorithm** | **Explanation** | **Unique Feature** |
|---------------|-----------------|--------------------|
| **Bubble Sort & Selection Sort** | Simple comparison sorts that repeatedly step through the list. | **Intuitive but inefficient:** Easy to understand, but slow (`O(n²)`) for large lists. |
| **Merge Sort & Quick Sort** | Efficient, “Divide and Conquer” algorithms that break the problem into smaller pieces. | **Fast for general use:** Achieves optimal average time complexity of `O(n log n)`. |
| **Counting Sort & Radix Sort** | Non-comparison sorts that leverage specific properties of the data (e.g., integer ranges) to sort faster. | **Extremely fast:** Can achieve linear time `O(n)` complexity under specific conditions. |

---


## 📘 Repository Information

**Repository Developed by:** *Ayngaran Krishnamurthy*  
**Purpose:** Educational reference for understanding fundamental Data Structures and Algorithms concepts.  
*Not intended to be used for monetary benefits by any third party.*