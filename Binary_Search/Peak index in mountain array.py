class Solution:
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1
        possible_ans = 0
        while start <= end:
            mid = int(start + (end - start) / 2)
            if mid > 0 and arr[mid - 1] > arr[mid]:
                possible_ans = mid - 1
                end = mid - 1
            else:
                possible_ans = mid
                start = mid + 1
        return possible_ans


if __name__ == '__main__':
    input_arr = [0, 1, 0]
    print(Solution().peakIndexInMountainArray(input_arr))