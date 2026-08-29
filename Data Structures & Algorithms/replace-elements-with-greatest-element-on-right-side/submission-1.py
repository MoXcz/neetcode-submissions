class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        m = arr[n - 1]
        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]
            arr[i] = m
            m = max(m, val)
        arr[n - 1] = -1
        return arr
