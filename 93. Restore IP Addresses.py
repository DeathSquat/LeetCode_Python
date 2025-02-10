class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                res.append(".".join(path))
                return
            if len(path) > 4:
                return
            
            for end in range(start, min(start + 3, len(s))):
                segment = s[start:end + 1]
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(end + 1, path + [segment])

        backtrack(0, [])
        return res
