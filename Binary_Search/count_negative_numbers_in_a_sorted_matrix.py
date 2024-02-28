class Solution:
    def countNegatives(self, grid) -> int:

        if not grid:
            return 0

        lb = 0
        up = len(grid[0]) - 1
        ans = 0
        while lb <= len(grid) - 1 and up >= 0:
            if grid[lb][up] < 0:
                up -= 1
                ans += len(grid) - lb
            else:
                lb += 1
        return ans

if __name__ == '__main__':
    input_arr = [[]]
    print(Solution().countNegatives(input_arr))


