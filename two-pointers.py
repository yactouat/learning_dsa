from memory_profiler import profile
import random
from time import time
from typing import List

@profile
def sort_squares(nums: List[int]) -> List[int]:
    # fill array with zeroes
    n = len(nums)
    # `*` with a list repeats the element in the list `n` times
    result = [0] * n

    left, right = 0, n - 1
    curr_pos = n - 1
    
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        
        if left_square > right_square:
            result[curr_pos] = left_square
            left += 1
        else:
            result[curr_pos] = right_square
            right -= 1
        curr_pos -= 1
    
    return result

@profile
def sort_squares2(nums: List[int]) -> List[int]:
    nums = [num ** 2 for num in nums]
    nums.sort()
    return nums


inputs = []
for _ in range(100):
    length = random.randint(1, 100) 
    nums = []
    for _ in range(length):
        nums.append(random.randint(-100, 100))
    inputs.append(nums)

# select a random input
input = inputs[random.randint(0, len(inputs) - 1)]

sort_squares_time = 0
print("profiling `sort_squares`:")
start_time = time()
sort_squares(input)
end_time = time()
sort_squares_time += end_time - start_time

sort_squares2_time = 0
print("\nprofiling `sort_squares2`:")
start_time = time()
sort_squares2(input)
end_time = time()
sort_squares2_time += end_time - start_time

print(f"time taken for `sort_squares`: {sort_squares_time} seconds")
print(f"time taken for `sort_squares2`: {sort_squares2_time} seconds")

# second function performs better because it uses Python'sbuilt-in sorting algorithm
    