class Solution:
  def pattern(self,n):
    for i in range(n):
      for j in range(n):
        print("*", end="")
      print()
m=Solution()
n=6
m.pattern(n)

  ##time complexity:o(N^2), since we print N stars for each of the N rows.
  ##space complexity:O(1), no additional space is used apart from loop variables.
