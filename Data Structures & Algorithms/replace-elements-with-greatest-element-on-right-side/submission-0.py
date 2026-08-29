class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            m = 0
            for j in range(i+1, len(arr)):
                m = max(m, arr[j])
                arr[i] = m
        return arr
