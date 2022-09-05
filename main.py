# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<= right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                 left=mid+1
            else:
                right=mid-1
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 9]
    target = 9
    Solution.search(nums, target)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
