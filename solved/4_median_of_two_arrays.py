class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1    
        if nums1 == []: return (nums2[len(nums2)//2] + nums2[(len(nums2) - 1)//2])/2
        n, m, left, right, result, ext = len(nums1) - 1, len(nums2) + 3, 0, len(nums1) - 1, [], [(nums1[0] + 1), (nums1[-1] -1)]
        nums2.extend(ext)
        ext.extend(nums2)
        nums2 = ext
        #print (nums2)
        if nums1[0] >= nums2[(m + n + 1)//2]: result = [nums2[(m + n + 1)//2], min(nums1[0], nums2[(m + n + 1)//2 + 1])]
        elif nums1[n] <= nums2[(m - n + 1)//2]: result = [max(nums2[(m - n + 1)//2 - 1], nums1[n]), nums2[(m - n + 1)//2]]
        else:
            preleft = left
            while right > left:
                if nums1[left] < nums2[(m + n + 1)//2 - left]:
                    preleft = left
                    left = (left + right + 1)//2
                elif nums1[left] > nums2[(m + n + 1)//2 - left]:
                    right = (left + right)//2
                    left = preleft
                else: return nums1[left]
                if left == right: result = [max(nums1[left-1], nums2[(m + n + 1)//2 - left]), min(nums1[left], nums2[(m + n + 1)//2 - left + 1])]
                #print (left, right)
        #print (result)
        if (m + n)%2: return result[0]
        else: return (result[0] + result[1])/2
        
        
        
print (2, Solution().findMedianSortedArrays([],[1,2,3]))
print (4.5, Solution().findMedianSortedArrays([1,6,7,8],[2,3,4,5]))
print (4, Solution().findMedianSortedArrays([1,5,6],[2,3,4,7]))
print (3.5, Solution().findMedianSortedArrays([1,4,5],[2,3,6]))
print (3.5, Solution().findMedianSortedArrays([1,2],[3,4,5,6]))
print (2.5, Solution().findMedianSortedArrays([1],[2,3,4]))
print (2, Solution().findMedianSortedArrays([1,1,3,3],[1,1,3,3]))
