---
# 题目一

## 方法一

### my solution
```python
```
### issues

### modify
```python
```
### correct
```python
```
---

# 0001. 两数之和

## 题目

- 给一个整数数组，和一个目标值
- 找出是否存在两个数值之和，为给定目标值
- 返回两个数值的 index 组合
- 只会存在一个有效答案

## 枚举法

### my solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for fist_index, first_value in nums[:-1]:
            for second_index, second_value in nums[1:]:
                if fist_value + second_value == target:
                    return [first_index, second_index]

        return []

nums = [2,7,11,15]
target = 9
```

### issues

- list 第 1 个到倒数第 2 个: array[:-1]
- list 第 2 个到倒最后 1 个: array[1:]
- 如果没找到, 应该返回空, return []

### modify

- enumerate() 才有 index + value
- range()
- 第二个循环应该从第一个 index 的下一位开始

```python
class Solution(object):
    def twoSum(self, nums, target):
        for first_index, first_value in enumerate(nums[:-1]):
            for second_index in range(first_index + 1, len(nums)):
                second_value = nums[second_index]
                if first_value + second_value == target:
                    return [first_index, second_index]

        return []
```

- first_index + 1 + second_index

```python
class Solution(object):
    def twoSum(self, nums, target):
        for first_index, first_value in enumerate(nums[:-1]):
            for second_index, second_value in enumerate(nums[first_index + 1:]):
                if first_value + second_value == target:
                    return [first_index, first_index + 1 + second_index]

        return []
```

### correct

```python
class Solution(object):
    def twoSum(self, nums, target):
        for fist_index, first_value in nums[:-1]:
            for second_index, second_value in range(first_index + 1, len(nums)):
                if fist_value + second_value == target:
                    return [first_index, second_index]

        return []
```

## Hash Table

### my solution

```Python
class Solution(object):
    def twoSum(self, nums, target):
        dict = []

        for index in range(len(nums)):
            if target - nums[index] exist in dict:
                return [dict[target - nums[index]], index]

        return []
```

### issues

- numDict = dict()
- if ... in numDict:
- 如果没有匹配, 应该将当前的值和 index 存入目标字典

### modify

```python
class Solution(object):
    def twoSum(self, nums, target):
        tempDict = dict()

        for index in range(len(nums)):
            if target - nums[index] in tempDict:
                return [tempDict[target - nums[index]], index]
            tempDict[nums[index]] = index

        return []
```

# 0009. 回文数

## 纯数学

### 思路

- 复数, 10 的倍数且不是 0, 返回 false
- 将数字的后半部分反转 res
  - 每次取 input x 的最后一位: 取 x 的 10 的余数
- while x > res
  - 给 res 添加 x 的最后一位: res \* 10 + 最后一位
- x == res or x == res // 10

### modify

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10
        return x == res or x == res // 10

x = 121
```

# 0013. 罗马数字转整数

## 题目

- 罗马数字，字符串
- 如果后一位，比前一位大，后一位减去前一位，否则相加

## 哈希表、数学、字符串

### my solution

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int_map = {'I': 1, 'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        total = 0
        pointer = 0

        while pointer < s.length():
            first_value = roman_int_map[s[pointer]]
            second_value = roman_int_map[s[pointer + 1]]

            if  first_value < second_value:
                total = total + second_value - first_value
                pointer = pointer + 2
            else:
                total = total + first_value
                pointer = pointer + 1

        return total
```

### issues

- s.length() ---> len(s)
- 需要检查下一个 char 是否存在，如果不存在就直接将 first_value 加上，pointer 加一
- total = total + second_value - first_value ---> total += second_value - first_value

### modify

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int_map = {'I': 1, 'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        total = 0
        pointer = 0

        while pointer < len(s):
            first_value = roman_int_map[s[pointer]]

            if pointer + 1 < len(s):
                second_value = roman_int_map[s[pointer + 1]]

                if  first_value < second_value:
                    total += second_value - first_value
                    pointer = pointer + 2
                else:
                    total += first_value
                    pointer = pointer + 1
            else:
                total += first_value
                pointer = pointer + 1

        return total
```

### correct logic

- 我的方法，从思路层面就是错误的
- 不用管罗马数字的规则，就按照下述算法进行
- 遍历字符串，如果一个比下一个小，就减去，否则就加上
- index 移动到下一个

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {'I': 1, 'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        total = 0
        first_value = roman_int_map[s[0]]

        for i in range(1, len(s)):
            second_value = roman_int_map[s[i]]

            if  first_value < second_value:
                total -= first_value
            else:
                total += first_value

            first_value = second_value

        total += firstr_value

        return total
```

# 0014. 最长公共前缀

## 方法一

### my solution

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ""
        for i in range(strs[0].length):
            exist_common_char = True
            common_char = strs[0][i]
            for j in range(strs.length):
                if not strs[j][i] or strs[j][i] != common_char:
                    exist_common_chart = False
                    break
            if exist_common_char = True:
                common_prefix += common_char
        return common_prefix
```

### issues

- strs[0].length 应改为 len(strs[0])。
- strs.length 应改为 len(strs)。
- if exist_common_char = True: 应改为 if exist_common_char:。
- not strs[j][i] ---> i > len(strs[j])
- if exist_common_char: common_prefix += common_char else: break

### modify

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        common_prefix = ""
        for i in range(len(strs[0])):
            exist_common_char = True
            common_char = strs[0][i]
            for j in range(len(strs)):
                if i > len(strs[j]) or strs[j][i] != common_char:
                    exist_common_chart = False
                    break
            if exist_common_char: common_prefix += common_char
            else: break
        return common_prefix
```

### correct algorithm

- 首先检查输入列表是否为空，如果为空则返回空字符串。
- 取第一个字符串的长度作为基准长度，并获取字符串的数量。
- 遍历第一个字符串的每个字符，并与其他字符串相同位置的字符进行比较。
- 如果在某个位置字符不匹配或达到某个字符串的末尾，返回到当前位置的子串作为公共前缀。
- 如果遍历完第一个字符串的所有字符都没有返回，说明第一个字符串是公共前缀，直接返回。

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        basic_length = len(strs[0])
        count = len(strs)

        for i in range(basic_length):
            for j in range(1, count):
                if len(strs[j]) == i or strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
```

- range(0, basic_length) ---> range(basic_length)
- 最后如果 if 没 return，需要 return strs[0]
- len(strs[j]) < i ---> len(strs[j]) == i
