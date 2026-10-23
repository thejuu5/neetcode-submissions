class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        i = 0
        j = len(cleaned) - 1
        if cleaned == "":
            return True
        while(i < j):
            if cleaned[i] == cleaned[j]:
                i = i+1
                j = j-1
            else:
                return False
        return True


            

        