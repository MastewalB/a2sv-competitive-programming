def PredictTheWinner(nums):
    if len(nums) == 1:
        return True

    def predict(start, end):
        if start == end:
            return nums[start]
        return max(nums[start] - predict(start + 1, end), nums[end] - predict(start, end - 1))

    result = predict(0, len(nums) - 1)
    return a >= 0
