class Solution:

    def sortArrayByParity(self, A: List[int]) -> List[int]:

        i=0

        n=len(A)-1

        while i<n:

            if A[n]%2!=0:

                n-=1

            if A[i]%2==0:

                i+=1

                continue

            if A[i]%2!=0 and A[n]%2==0:

                A[i],A[n]=A[n],A[i]

                n-=1

                i+=1

        return A
