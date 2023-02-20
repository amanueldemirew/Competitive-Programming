class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left,m,counter,=0,0,0
        vowels=['a','e','i','o','u']
        
        for right in range(len(s)):
            if s[right] in vowels:
                counter+=1
            if right-left+1==k:
                m=max(m,counter)
                if s[left] in vowels:
                    counter-=1
                left+=1
        return m