class Solution:
    def pattern(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(i, end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    n = 5
    sol.pattern(n)
  ##time Complexity:o(n^2)
  ##space Complexity:o(1)

##output
1
22
333
4444
55555
