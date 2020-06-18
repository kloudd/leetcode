class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:

        for i in range(0,len(arr)):

            for j in range(i+1,len(arr)):

                if ((arr[i] == arr[j] * 2) or (arr[i] == arr[j] * 0.5)):

                    return True

        return False
