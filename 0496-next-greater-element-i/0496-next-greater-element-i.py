class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        out = [-1]*len(nums1)
        for j in range(len(nums1)):
            x = nums2.index(nums1[j])
            
            for i in range(x+1,len(nums2)):
                
                if nums2[i] > nums1[j]:
                    out[j] = nums2[i]
                    break
                    
            
        return out
                    
                
        
      