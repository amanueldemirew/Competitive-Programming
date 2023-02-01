class Solution:
    def evalRPN(self, token: List[str]) -> int:
               
        out = []
        for i in token:
            if i not in "+/*-":
                out.append(int(i))
            else:
                y, x = out.pop(), out.pop()
                if i == "+":
                    out.append(x + y)
                elif i == "-":
                    out.append(x - y)
                elif i == "*":
                    out.append(x * y)
                else:
                    out.append(int(x / y))        
        return out[0]

            
            
        