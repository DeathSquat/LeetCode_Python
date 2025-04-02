class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        
        # Dictionary to store sequence counts
        seen = {}
        result = []
        
        # Slide window of size 10 across the string
        for i in range(len(s) - 9):
            current_seq = s[i:i+10]
            # If sequence seen before, add to result if it's the second occurrence
            if current_seq in seen:
                if seen[current_seq] == 1:
                    result.append(current_seq)
                seen[current_seq] += 1
            else:
                seen[current_seq] = 1
                
        return result
