#17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        out1 = []
        out2 = []
        for c in digits:
            n = ord(c)
            newc = []
            if n>49 and n<55:
                newc = [chr(-53 + n*3), chr(-52 + n*3), chr(-51 + n*3)]
            if n == 55:
                newc = [chr(-53 + n*3), chr(-52 + n*3), chr(-51 + n*3), chr(-50 + n*3)]
            if n == 56:
                newc = [chr(-52 + n*3), chr(-51 + n*3), chr(-50 + n*3)]
            if n == 57:
                newc = [chr(-52 + n*3), chr(-51 + n*3), chr(-50 + n*3), chr(-49 + n*3)]
                
            #print (newc)
            
            if out1 == []:
                out2 = newc
            else:
                for cc in out1:
                    for ccc in newc:
                        out2.append(cc + ccc)
            out1 = out2
            out2 = []
            
        #print (ord('1'))
            
        return out1
        
        
print (Solution().letterCombinations("23"))