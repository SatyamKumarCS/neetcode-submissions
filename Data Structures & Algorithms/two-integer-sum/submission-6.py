class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort(key=lambda x: x[0])
        l = 0
        r = len(arr) - 1

        while l < r:
            total = arr[l][0] + arr[r][0]
            if total == target:
                return sorted([arr[l][1], arr[r][1]])
            elif total > target:
                r -= 1
            else:
                l += 1
        return []