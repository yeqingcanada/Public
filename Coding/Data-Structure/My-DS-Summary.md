# Linked List

```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

# Stack

- stack = []
- stack.append()
- stack.pop()

# Queue

```python
self.queue = []
self.queue.pop(0)
self.queue.append(val)
```

# HashTable

numDict = dict()

# Tree

```python
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

# Graph

二维数组  
graph = [[1,2],[3],[3],[]]

# Sorting

- Bubble Sort: 每一轮都会将一个元素排好，比如说，第一轮，将最大值排到最后一位，第二轮，将倒数第二大值排到倒数第二位。O(n^2)
- Selection Sort：每一轮从未排序部分中选出最小（或最大）的元素，将其放在已排序部分的末尾。O(n^2)
- Insertion Sort：通过构建有序序列，将未排序部分中的元素一个一个插入到已排序部分的适当位置，从而得到一个新的、稍大的有序序列。O(n^2)
- Merge Sort
- Quick Sort
- Counting Sort
- Bucket Sort
- 堆排序
- 希尔排序
- 基数排序

# Searching

- Linear Search：逐个检查列表中的每个元素，直到找到目标元素或者列表的末尾。O(n)
- Binary Search
- Ternary Search
- Jump Search
- Exponential Search
