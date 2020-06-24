'''
搜索旋转排序数组

算法时间复杂度必须是 O(log n) 级别。

'''

class Solution:
    # 二分法(循环版）
    def search(self, nums, target):
        # nums 为空时，直接返回 -1
        if not nums:  # = if nums is None
            return -1

        # 初始左右边界
        left, right = 0, len(nums) - 1

        # 判断哪部分区间是有序的
        # 判断 target 会落在哪个区间
        while left <= right:
            # 数组划分为两部分
            mid = (left + right) // 2
            # 如果目标值与划分区间的元素相等时，直接返回
            if nums[mid] == target:
                return mid

            # 判断区间是否有序
            # 这里表示 [left, mid - 1] 是有序的
            if nums[0] <= nums[mid]:
                # target 落在 [left, mid - 1] 这个区间
                if nums[0] <= target < nums[mid]:
                    # 重新划分右边界
                    right = mid - 1
                # target 落在 [mid + 1, right] 这个区间
                else:
                    # 重新划分左边界
                    left = mid + 1

            # nums[0] > nums[mid] 时，表示 [mid + 1, right] 有序
            else:
                # target 落在 [mid + 1, right] 时
                if nums[mid] < target <= nums[right]:
                    # 重新划分左边界
                    left = mid + 1
                else:
                    # target 落在 [left, mid - 1] 这个区间
                    # 重新划分左边界
                    right = mid - 1

        return -1

    # 二分法（递归版）
    def search1(self, nums, target):
        def search(nums, left, right, target):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return search(nums, left, mid-1, target)
                else:
                    return search(nums, mid+1, right, target)
            else:
                if nums[mid] < target <= nums[right]:
                    return search(nums, mid+1, right, target)
                else:
                    return search(nums, left, mid-1, target)
        return search(nums, 0, len(nums), target)





if __name__ == '__main__':
    nums  = [4, 5, 6, 7, 0, 1, 2]
    s = Solution()
    res = s.search1(nums,0)
    print(res)