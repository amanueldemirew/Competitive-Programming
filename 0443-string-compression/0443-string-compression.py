class Solution:
    def compress(self, chars: List[str]) -> int:
        length, count = 0, 1
        chars.append("##")
        
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                chars[length] = chars[i-1]
                length += 1
                if count > 1:
                    for ch in str(count):
                        chars[length] = ch
                        length += 1
                count = 1
        
        return length