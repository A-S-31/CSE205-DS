class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Initialize max_sum with the first element of the array.
        current_sum = nums[0]  # Initialize current_sum with the first element of the array.

        for num in nums[1:]:
            # Compare the current element with the sum of the current element and the current_sum.
            # Choose the maximum between them as the new current_sum.
            current_sum = max(num, current_sum + num)

            # Update max_sum if the current_sum becomes larger.
            max_sum = max(max_sum, current_sum)

        return max_sum

   