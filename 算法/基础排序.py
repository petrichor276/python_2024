nums = [2, 7, 11, 15]

target = 9
p1 = 0
result = []
records = dict()

for i in range(len(nums)):
    for j in range(len(nums)):
        if j + 1 and i != j and i < j:
            if nums[i] + nums[j] == target:
                result.append([i, j])
# print(result)
for idx, val in enumerate(nums):
    # print(idx, val)
    if target - val not in records:
        # print(target - val)
        records[val] = idx
        # print(records)
    else:
        b = [records[target - val], idx]
        # print(records)


# print()
# print(b)
# print(records)
class Solution:

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 排序后存放的位置
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted
        print(nums1)


# 创建 Solution 的实例
solution = Solution()
solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
