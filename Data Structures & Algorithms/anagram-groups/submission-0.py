class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = list()
        while len(strs) > 0:
            curr = strs.pop()
            found = False
            for lst in out:
                if sorted(curr) == sorted(lst[0]):
                    lst.append(curr)
                    found = True
                    break
            if found == False:
                out.append([curr])
        return out
            

        
        