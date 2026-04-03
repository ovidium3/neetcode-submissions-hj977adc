class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = {}

        for st in strs:
            newSt = ''.join(sorted(st)) # sorted returns a list, so convert to str using ''.join()
            if newSt in resMap:
                resMap[newSt].append(st)
            else:
                resMap[newSt] = [st]
        
        retList = []
        
        for k, v in resMap.items():
            retList.append(v)

        return retList