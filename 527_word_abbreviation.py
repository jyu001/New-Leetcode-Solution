'''
527. Word Abbreviation
DescriptionHintsSubmissionsDiscussSolution
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.
'''


class Solution:
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        indx = {word:index for index, word in enumerate(dict)}
        dct = {}
        for w in dict:
            n, indexw = len(w), indx[w]
            if n < 4: dct[w] = [dict[indexw]]
            else:
                nw = w[0] + str(n-2) + w[-1]
                if nw in dct: dct[nw].append(dict[indexw])
                else: dct[nw] = [dict[indexw]]
        res = [0]*len(dict)
        #print(dct)
        for short, listw in iter(dct.items()):
            #print(short, listw)
            if len(listw) == 1: res[indx[listw[0]]] = short
            else:
                newlist = sorted(listw)
                pre, l = 0, len(newlist[0])-2
                if l==2: 
                    for w in newlist: res[indx[w]] = w
                    continue
                for i in range(len(newlist)-1):
                    for j in range(1, l+2):
                        w, v = newlist[i], newlist[i+1]
                        if w[j] == v[j]: continue
                        else:
                            n, pre = max(pre, j+1), j+1
                            if n< l: res[indx[newlist[i]]] = w[:n] + str(l - n + 1) + w[-1]
                            else: res[indx[newlist[i]]] = w
                            break
                w = newlist[-1]
                if pre<l: res[indx[newlist[-1]]] = w[:pre] + str(l - pre + 1) + w[-1]
                else: res[indx[newlist[-1]]] = w
        return res