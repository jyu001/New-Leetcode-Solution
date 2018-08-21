'''
241. Different Ways to Add Parentheses
DescriptionHintsSubmissionsDiscussSolution
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

'''

return [a+b if c=='+' else a-b if c=='-' else a*b
            for i,c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])
            ] or [int(input)]



'''
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # for each operator, there are two possible ways, 2 - (1-1) and (2-1) -1
        
        dct = {'+':0,'-':1,'*':2}
        lst = []
        curr = 0
        for i in range(len(input)):
            if input[i] in dct:
                lst.append(int(input[curr:i]))
                lst.append(dct[input[i]])
                curr = i+1
        lst.append(int(input[curr:]))
        
        def check(lst):
            if len(lst) == 1: return [lst[0]]
            elif len(lst) == 3:
                a,b,c = lst
                res = [a+c, a-c, a*c]
                return [res[b]]
            else:
                l1 = check(lst[2:])
                l2 = check(lst[:3])
                res = []
                for ll in l1:
                    res += check(lst[:2]+[ll])
                res += check([l2[0]]+lst[3:])
            return res
        
        return check(lst)
                
'''