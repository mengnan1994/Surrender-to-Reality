# coding: utf-8
# (i.e., [0,1,2,4,5,6,7] might become [4, 5, 6, 7, 0, 1, 2]).
# no duplicate exists
# binary search


class Solution:

    # don't use this solution, its trash
    def search2(self, nums, target):
        # cases:
        # 0. == mid, bingo!
        # 1. < left, < mid, <= right,  [mid+1, right] ???
        # 2. < left, < mid, > right ,  return -1
        # 3. < left, > mid, <= right,  [mid+1, right]
        # 4. < left, > mid, > right ,  return -1
        # 5. >= left, < mid, <= right, [left, mid-1]
        # 6. >= left, < mid, > right,  [left, mid-1]
        # 7. >= left, > mid, <= right, [mid+1, right]
        # 8. >= left, > mid, > right,  [left, mid-1] ???
        print(nums, target)
        if len(nums) == 0:
            return -1
        elif len(nums) == 1 and target == nums[0]:
            return 0
        elif len(nums) == 1 and target != nums[0]:
            return -1

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            print("=======")
            print(left, mid, right)
            print(nums[left], nums[mid], nums[right])

            if target == nums[mid]:
                return mid
            elif target < nums[left] and target < nums[mid] and target <= nums[right]:
                if nums[left] < nums[mid]:
                    left = mid + 1
                    mid = (left + right) // 2
                else:
                    right = mid - 1
                    mid = (left + right) // 2
            elif target < nums[left] and target < nums[mid] and target > nums[right]:
                return -1
            elif target < nums[left] and target > nums[mid] and target <= nums[right]:
                left = mid + 1
                mid = (left + right) // 2
            elif target < nums[left] and target > nums[mid] and target > nums[right]:
                return -1
            elif target >= nums[left] and target < nums[mid] and target <= nums[right]:
                right = mid - 1
                mid = (left + right) // 2
            elif target >= nums[left] and target < nums[mid] and target > nums[right]:
                right = mid - 1
                mid = (left + right) // 2
            elif target >= nums[left] and target > nums[mid] and target <= nums[right]:
                left = mid + 1
                mid = (left + right) // 2
            elif target >= nums[left] and target > nums[mid] and target > nums[right]:
                if nums[mid] < nums[left]:
                    right = mid - 1
                    mid = (left + right) // 2
                else:
                    left = mid + 1
                    mid = (left + right) // 2
        return -1

    def search(self, nums, target):
        # still not accepted
        # im enough with this idiot
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        mid = left + (right - left) // 2
        while left <= right:
            print("========================")
            print("left\tmid\tright")
            print("{}\t{}\t{}".format(nums[left], nums[mid], nums[right]))
            if target == nums[mid]:
                return mid
            elif nums[mid] < nums[right]:  # right half sorted
                if target > nums[mid] and target <= nums[right]:  # target may be on right side
                    left = mid + 1
                    mid = left + (right - left) // 2
                else:  # target may be on left side
                    right = mid - 1
                    mid = left + (right - left) // 2
            elif nums[mid] > nums[left]:  # left half sorted
                if target < nums[mid] and target >= nums[left]:  # target may be on left side
                    right = mid - 1
                    mid = left + (right - left) // 2
                else:
                    left = mid + 1
                    mid = left + (right - left) // 2

        return -1


sol = Solution()
nums = [3,1]
target = 0
print(sol.search(nums, target))