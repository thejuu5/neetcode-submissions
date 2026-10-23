class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        if strs == "":
            return ""
        for i in range (0,len(strs)):
            encode_str += str(len(strs[i])) + "#" + strs[i]
        return encode_str
            

    def decode(self, s: str) -> List[str]:
        decode_list = []
        if s == "":
            return decode_list
        i = 0
        while i < len(s):
            pos = s.find('#',i)
            length = int(s[i:pos])
            decode_list.append(s[pos+1:pos+length+1]) 
            i = pos+length+1
            
            
        return decode_list
