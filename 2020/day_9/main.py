import numpy as np
import time as t

def task_1(nums) :
  preamble = 25
  n = len(nums)

  for i in range(preamble, n) :
    val = nums[i]
    s = set()
    for o in range(i - preamble, i) :
      s.add(nums[o])
    
    P = lambda x : (val - x) in s 
    if not any(P(x) for x in s) :
      return val
    
  return -1

def task_2_inefficient(nums, val) :
  n = len(nums)
  for i in range(n) :
    for j in range(i + 1, n) :
      if sum(nums[i:j + 1]) == val :
        return max(nums[i:j + 1]) + min(nums[i:j + 1])
  return -1
  
# time complexity: O(n^2)
def task_2(nums, val) :
  n = len(nums)
  # triangular dp matrix
  # dp[i][j] : sum from i to j from nums[]
  # dp[i][j] = dp[i][j - 1] + nums[j] for j > i
  # dp[i][i] = nums[i]
  dp = np.empty((n,n), dtype=int)

  for i in range(n) :
    dp[i][i] = nums[i]

  for i in range(0, n) :
    for j in range(i + 1, n) :
      dp[i][j] = dp[i][j - 1] + nums[j]
      if (dp[i][j] == val) :
        return max(nums[i:j + 1]) + min(nums[i:j + 1])

  return -1

def main() :
  with open("input_day_9.txt", 'r') as input_file :
    nums = []
    for line in input_file :
      nums.append(int(line.strip("\n")))
    val = task_1(nums)
    print(f"Task 1: {val}")
    t1 = t.time()
    print(f"Task 2: {task_2(nums, val)}")
    t2 = t.time()
    print(f"Task 2: {task_2_inefficient(nums, val)}")
    t3 = t.time()

    print(f"time task 2 fast: {t2 - t1}, time task 2 inefficient: {t3 - t2}")
    

if __name__ == "__main__":
  main()