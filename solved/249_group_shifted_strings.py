'''
249. Group Shifted Strings
DescriptionHintsSubmissionsDiscussSolution
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic  = {}
        if strings == '':return []
        for s in strings:
            n = ord(s[0])
            if len(s) == 1 and 1 not in dic:
                dic[1] = [s]
                continue
            elif len(s) == 1 and  1 in dic:
                dic[1].append(s)
                continue
            token = ''
            for c in s:
                m = ord(c) - n
                if m >= 0:
                    token += str(99-m)
                else:
                    token += str(99-26 - m)
            if token not in dic:
                dic[token] = [s]
            else:dic[token].append(s)
            token = ''
        res = []
        for i in dic:
            res.append(dic[i])
        return res