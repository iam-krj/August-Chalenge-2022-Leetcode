from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        w_map = defaultdict(int)
        for i in magazine :
            w_map[i]+=1
        for i in ransomNote :
            if w_map[i] == 0 :
                return False
            w_map[i]-=1
        return True
