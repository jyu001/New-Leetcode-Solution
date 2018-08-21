'''
692. Top K Frequent Words
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
'''

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dct = {}
        for w in words:
            if w not in dct: dct[w]=0
            dct[w] += 1
        new = {}
        for w,n in dct.items():
            if n not in new: new[n] = []
            new[n].append(w)
        lst = sorted(new.items(), key=lambda x:x[0])
        res = []
        while k>0:
            #print (res, lst)
            a = lst.pop(-1)
            if len(a[1]) > k:
                res += sorted(a[1])[:k]
                k = 0
            else:
                res += sorted(a[1])
                k -= len(a[1])
        return res