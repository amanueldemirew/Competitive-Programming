class Solution:
    def sortSentence(self, s: str) -> str:

        words = s.split(" ")
        sortsent =""
        n = len(words) 

        for i in range(n):
            
            min = i
           
            for j in range(i+1,n):
                
                if words[j][-1] < words[min][-1]:
                   
                    min = j
            
            if i != min:
                
                words[min] ,words[i]  = words[i] ,words[min]

            sortsent += words[i][:-1] + " "
        
        return (sortsent[:-1])
