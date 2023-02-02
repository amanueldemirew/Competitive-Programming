class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        Q = []
        for c in s : 
            if c!=')' :
                stack.append(c)
            else:
                d= stack.pop()
                while d!='(':
                    Q.append(d)
                    d=stack.pop()
                while  Q :
                    stack.append(Q.pop(0))       
        rev_s = "".join(stack)
        return rev_s
            


        
        