class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:

        l = len(arr)

        cache_current = maximum = arr[-1]

        for i in range(l - 2, -1, -1):

            cache_current = arr[i]

            arr[i] = maximum

            maximum = max(maximum, cache_current)

        arr[-1] = -1

        return arr
