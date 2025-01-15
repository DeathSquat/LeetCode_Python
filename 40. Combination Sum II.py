class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, target, path, res):
            # Base case: if the target becomes 0, we found a combination
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the candidate exceeds the target, skip it
                if candidates[i] > target:
                    break
                
                # Include the candidate and backtrack
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path, res)
                path.pop()  # Undo the choice

        candidates.sort()  # Sort to handle duplicates
        result = []
        backtrack(0, target, [], result)
        return result
