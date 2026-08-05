class Solution:
  def RightAngle(self,n):
    for i in range(n):
      for j in range(i+1):
        print("*", end="")
      print()
m=Solution()
n=5
m.RightAngle(n)

## time complexity:o(n^2)
##space compelxtiy:O(1)
class Solution:
  def RightAngle(self,n):
    for i in range(n):
      for j in range(i+1):
        print("*", end="")
      print()
m=Solution()
n=3
m.RightAngle(n)
  
