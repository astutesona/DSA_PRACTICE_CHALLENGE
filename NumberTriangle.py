class Solution:
  def numberTriangle(self,n):
    for i in range(1,n+1):
      for j in range(1,i+1):
        print(j,end="")
      print()
m=Solution()
m.numberTriangle(5)
## Time Complexity: o(n^2)
## space Complexity:o(1)
