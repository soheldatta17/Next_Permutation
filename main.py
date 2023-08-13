class Solution:
  
    def nextPermutation(self, N, arr):
      
        if N==0:
            return
        if N==1:
            return arr
        k=N-2
        for i in range(N-1,0,-1):
            if arr[i]<=arr[i-1]:
                k-=1
            else:
                break
        if k==-1:
            return arr[::-1]
            
        for i in range(N-1,0,-1):
            if arr[i]>arr[k]:
                arr[i],arr[k]=arr[k],arr[i]
                break
        return arr[0:k+1]+arr[:k:-1]
