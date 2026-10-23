class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = {}
        if strs is " ":
            return [""]
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in dict_strs:
                dict_strs[sorted_word].append(str(word))
            else:
                dict_strs[sorted_word] = [str(word)]
        return list(dict_strs.values())

    