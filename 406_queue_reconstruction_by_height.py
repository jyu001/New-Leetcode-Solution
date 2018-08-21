'''
406. Queue Reconstruction by Height
DescriptionHintsSubmissionsDiscussSolution
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # first put the highest people, [7,0], [7,1]
        # then insert the next highest people, [6,1] to the index i=1 position
        # repeate
        if not people: return []
        people = sorted(people)
        j = i = len(people)-1
        res = []
        while i>=0:
            while j+1 and people[j][0] == people[i][0]: j-=1
            for k in range(j+1, i+1): res.insert(people[k][1], people[k])
            i = j
            #print(people, i, res)
        return res