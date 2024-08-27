# 01. 数组

## 02. 数组排序

### 01. 冒泡排序

```python
class Solution:
   def bubbleSort(self, nums: [int]) -> [int]:
      for i in range(len(nums)):
         if nums[i] > nums[i+1]:
            temp = nums[i+1]
            nums[i+1] = nums[i]
            nums[i] = temp
      return nums
```

- for loop 最后一位不是结尾，而是倒数第二位
- 1&2，2&3，3&4...n-1&n
- 1&2，2&3，3&4...n-2&n-1
- ......
- 交换 nums[j], nums[j+1] = nums[j+1], nums[j]
- 任何一趟(if not flag: break)，没有任何变化，都说明排序已经完成，break 跳出

```python
class Solution:
   def bubbleSort(self, nums: [int]) -> [int]:
      for i in range(len(nums) - 1):
         flag = False
         for j in range(len(nums) - i - 1):
            if nums[j] > nums[j+1]:
               nums[j], nums[j+1] = nums[j+1], nums[j]
               flag = True
         if not flag: break
      return nums
```

### 02. 选择排序

- 左侧为已排序区间，右侧为未排序区间
- start_index (min_index 的初始值) 每次向右移动一位
- 每趟找到 min_index，与这趟的 start_index 交换值

```python
class Solution:
   def selectionSort(self, nums: [int]) -> [int]:
      for i in range(len(nums) - 1):
         min_i = nums[i]
         for j in range(i + 1, len(nums) - 1):
            if nums[j] < min_i:
               min_i = nums[j]
               nums[i], nums[j] = nums[j], nums[i]

      return nums
```

- min_i 应该存储的是索引，而不是元素的值。
- 内层循环的范围应该包括列表的最后一个元素。
- 交换元素的操作应放在内层循环结束后，而不是在找到更小的元素时就交换。

```python
class Solution:
   def selectionSort(self, nums: [int]) -> [int]:
      for i in range(len(nums) - 1):
         min_i = i
         for j in range(i + 1, len(nums)):
            if nums[j] < muns[min_i]:
               min_i = j
         nums[i], nums[min_i] = nums[min_i], nums[i]

      return nums
```

### 03. 插入排序

### 04. 希尔排序

### 05. 归并排序

### 06. 快速排序

### 07. 堆排序

### 08. 计数排序

### 09. 桶排序

### 10. 基数排序

## 03. 数组二分查找

### 01. 二分查找知识（一）
