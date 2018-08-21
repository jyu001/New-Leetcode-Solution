'''
68. Text Justification
DescriptionHintsSubmissionsDiscussSolution
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

'''


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i = 0
        res = []
        while i<len(words):
            l = [words[i]]      # list of words index
            l2 = []     # list of space length
            wid, i = maxWidth - len(words[i]) - 1, i+1
            while i<len(words) and wid >= len(words[i]):
                l.append(words[i])
                wid -= len(words[i]) + 1
                i += 1
            wid += 1
            #print('i', i, 'l', l)
                
            n = len(l)
            if n==1: 
                res.append(l[0] + ' '*(maxWidth-len(l[0])))
            elif i == len(words):
                s = l[0]
                count = len(l[0])
                for w in l[1:]:
                    s += ' ' + w
                    count += 1 + len(w)
                res.append(s + ' '*(maxWidth-count))
            else:
                a, b = 1+wid//(n-1), wid%(n-1)
                for j in range(n-1):
                    if j<b: l2.append(' '*(a+1))
                    else: l2.append(' '*a)
                s = l[0]
                for j in range(len(l2)):
                    s += l2[j] + l[j+1] 
                res.append(s)
        return res