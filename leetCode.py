from typing import List
import math


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        for i, value in enumerate(nums):
            if value not in seen.keys():
                seen[value] = i

        print(nums)
        for i, value in enumerate(seen.keys()):
            nums.insert(i, value)
        return len(seen.keys())

    def maxProfit(self, prices: List[int]) -> int:
        sortedPrice = sorted(prices)
        if len(prices) == 1:
            return 0
        if prices[0] == sortedPrice[-1] and prices == sortedPrice:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    def reverse(self, nums: List[int], start, end):
        while start > end:
            nums[start], nums[end] = nums[end], nums[start]
            start = start+1
            end = end-1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        print(length)
        k = k % length
        self.reverse(nums, 0, length-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length-1)

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False

    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits))) + 1
        numStr = num.__str__()
        return list(numStr)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 1:
            return nums
        p1, p2, i = 0, 1, 1  # p1 is pointer for zero and p2 for other values
        while p1 < length:
            p2 = min(p2, length-1)
            if nums[p2] != 0 and nums[p1] == 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1, p2 = p2, p1
                p2 += 1
                if p2 == p1:
                    p2 += 1
            elif nums[p1] == 0 and nums[p2] == 0:
                if p1 > p2:
                    p1, p2 = p2, p1
                    p2 += 1
                else:
                    p2 += 1
                    if p2 == length:
                        p1 = length
            else:
                p1 += 1
                p2 += 1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 2):
            return [0, 1]
        for i in range(int(len(nums)/2) + 1):
            noToFind = target - nums[i]
            n = nums.copy()
            n.pop(i)
            count = n.count(noToFind)
            if count > 0:
                index = nums.index(noToFind, i+1)
                if (i != index):
                    return [i, index]
            noToFind = target - nums[-i]
            count = nums.count(noToFind)
            if count > 0:
                index = nums.index(noToFind)
                index2 = nums.index(nums[-i])
                if (index2 != index):
                    if index > index2:
                        return [index2, index]
                    return [index, index2]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)  # key=> (r//3,c//3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3, c//3)]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])

        return True

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r-l):
                t, b = l, r
                print(matrix[t][l+i], matrix[b-i][l],
                      matrix[b][r-i], matrix[t+i][r])
                print(matrix[b-i][l], matrix[b][r-i],
                      matrix[t+i][r], matrix[t][l+i])
                matrix[t][l+i], matrix[b-i][l], matrix[b][r-i], matrix[t +
                                                                       i][r] = matrix[b-i][l], matrix[b][r-i], matrix[t+i][r], matrix[t][l+i]
            l += 1
            r -= 1

    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = x * -1
        r = int(str(x)[::-1])
        if abs(r) < 2**31 and r != 2**31 - 1:
            return -r if isNegative else r
        else:
            return 0
        return -r if isNegative else r

    def firstUniqChar(self, s: str) -> int:
        c = {}
        for i in range(len(s)):
            if s[i] in c:
                c[s[i]] = c[s[i]] + 1
            else:
                c[s[i]] = 1

        for i, value in enumerate(c):
            print(i, value)
            if c[value] == 1:
                return s.index(value)

        return -1

    def isAnagram(self, s: str, t: str) -> bool:
        sl, tl = list(s), list(t)
        sl.sort()
        tl.sort()
        if ''.join(sl) == ''.join(tl):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        revStr = ''.join(list(s)[::-1]).lower()
        return s == revStr

    def myAtoi(self, s: str) -> int:
        isNegative = None
        ints = []
        for index, value in enumerate(s):
            l = len(ints)
            if (value == '-' or value == '+') and (isNegative != None or l > 0):
                break
            if value == ' ' and isNegative != None:
                break
            if value == '-':
                isNegative = True
                continue
            if value == '+':
                isNegative = False
                continue
            if l == 0 and value == ' ':
                continue
            if value.isnumeric():
                ints.append(value)
            else:
                break
        if len(ints) == 0:
            return 0
        else:
            n = int(''.join(ints))
            n = -int(n) if isNegative else int(n)
            if n > (2**31) - 1:
                return 2**31 - 1
            if n < (-2**31):
                return -2**31
            else:
                return n

    def strStr(self, haystack: str, needle: str) -> int:
        h_len, n_len = len(haystack), len(needle)
        if n_len > h_len:
            return -1
        if h_len == n_len and haystack == needle:
            return 0
        if h_len == n_len and haystack != needle:
            return -1
        for i in range(h_len):
            if needle == haystack[i:n_len+i]:
                return i
        return -1

    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        current = ""

        strs = sorted(strs, key=len)
        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if strs[i] == "":
                    return ""
                if i == 0:
                    current = strs[i][j]
                    continue
                if strs[i][j] != current:
                    current = ""
                    return common
            common = common + current
        return common


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))

# haystack = "hello"
# needle = "ll"
# print(Solution().strStr(haystack, needle))
# s = "4193 with words"
# s = "-91283472332"
# s = "+-12"
# s = "00000-42a1234"
# s = "   -42"
# s = "  +  413"
# print(Solution().myAtoi(s))
# s = "A man, a plan, a canal: Panama"
# print(Solution().isPalindrome(s))
# s = "rat"
# t = "car"

# print(Solution().isAnagram(s, t))
# s = "leetcode"
# print(Solution().firstUniqChar(s))

# print(Solution().reverse(-1230))
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Solution().rotate(matrix)
# print(matrix)

# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]
# Solution().isValidSudoku(board)
# nums = [2, 7, 11, 15]
# target = 9
# print(Solution().twoSum(nums, target))

# nums = [0, 1, 1, 0]
# Solution().moveZeroes(nums)
# print(nums)
# nums = [8, 2, 0, 4, 5, 3, 2, 2, 6, 7, 3, 3,
#         6, 2, 9, 0, 8, 6, 2, 6, 9, 1, 2, 0, 2]
# print(Solution().plusOne(nums))

# nums = [3, 3]
# print(Solution().containsDuplicate(nums))


# nums = [8, 2, 0, 4, 5, 3, 2, 2, 6, 7, 3, 3,
#         6, 2, 9, 0, 8, 6, 2, 6, 9, 1, 2, 0, 2]
# k = 11939

# Solution().rotate(nums, k)
# # print((len(nums)))
# print(nums)


# prices = [7, 1, 5, 3, 6, 4, 8]
# x = Solution().maxProfit(prices)
# print(x)


# nums = [1, 1, 2]
# x = Solution().removeDuplicates(nums=nums)
# print(x)
# print(nums)
