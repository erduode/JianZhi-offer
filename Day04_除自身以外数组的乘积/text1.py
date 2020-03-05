'''
除自身以外数组的乘积
'''

class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int):
        i, j = 0, 0,

        while i < n:

            while j < len(nums1):
                if nums1[j] < nums2[i]:
                    j += 1
                elif j == len(nums1) - 1:

                    nums1.extend(nums2[+i:])
                else:
                    nums1.insert(j, nums2[i])
                    break

        i += 1
if __name__ == '__main__':
    # right = [1]*4
    # print(right)
    nums1 = [1,4,5]
    nums2 = [2,4,5,6]
    m = 3
    n = 4
    s = Solution()
    s.merge(nums1,3,nums2,4)
    print(nums1)
    # for i,value1 in enumerate(nums1):
    #     print(i,value1)
    #     for j,value2 in enumerate(nums2):
    #         if value1<value2:
    #             j+=1
    #         else:
    #             nums1.insert(i,value2)
    #             j+=1
    #             i+=1
    #     i+=1
    #
    # for i in nums3:
    #     print(i)

    i, j = 0, 0,

    # 当i，j的索引位置小于等于索引最大值的时候

    # while i < len(nums1):
    #     j = k
    #     while j < len(nums2):
    #
    #         if nums1[i] < nums2[j]:
    #             j += 1
    #         else:
    #             nums1.insert(i, nums2[j])
    #             k += 1
    #             j += 1
    #     i += 1






