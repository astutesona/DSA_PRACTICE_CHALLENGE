class Solution:
  def square(self, s):
    for i in range(s):
      for j in range(s):
        print("*", end="")
      print()
m=Solution()
s=2
m.square(s)
## time Complexity=o(s^2)
## space Complexity:o(1) 
