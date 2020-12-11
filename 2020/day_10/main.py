import numpy as np
import re

def task_1(adapters) :
  device_adapter = max(adapters) + 3
  adapters.append(device_adapter)
  n = len(adapters)
  sorted_adapters = np.sort(adapters)
  diffs = np.zeros(3, dtype=int)
  prev = 0

  for i in range(n) :
    curr_a = sorted_adapters[i]
    diff_index = curr_a - prev - 1
    diffs[diff_index] += 1
    prev = curr_a
  
  return diffs[0] * diffs[2]

# Time complexity O(nlogn)
def task_2(adapters) :
  device_adapter = max(adapters) + 3
  adapters.append(device_adapter)
  n = len(adapters)
  sorted_adapters = np.sort(adapters)
  adapters_set = set(sorted_adapters)
  dp = np.zeros(n, dtype=int)

  dp[n - 1] = 1
  dp[n - 2] = 1

  occ_a_1 = 1 if ((sorted_adapters[n - 2] - sorted_adapters[n - 3]) <= 3) else 0
  occ_a_2 = 1 if ((sorted_adapters[n - 1] - sorted_adapters[n - 3]) <= 3) else 0
  dp[n - 3] = occ_a_1 * dp[n - 2] + occ_a_2 * dp[n - 1]

  print(sorted_adapters)
  for i in range(n - 4, -1, -1) :
    curr_adapter = sorted_adapters[i]
    if (sorted_adapters[i + 3] - curr_adapter <= 3) :
      dp[i] = dp[i + 1] + dp[i + 2] + dp[i + 3]
    elif (sorted_adapters[i + 2] - curr_adapter <= 3) :
      dp[i] = dp[i + 1] + dp[i + 2]
    elif (sorted_adapters[i + 1] - curr_adapter <= 3) :
      dp[i] = dp[i + 1]
  
  return dp[0]


def main() :
  with open("input_day_10.txt", 'r') as input_file :
    adapters = [int(line) for line in input_file]
    
    test = [0, 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
    test_2 = [0, 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4 ]
    print(f"Task 1: {task_1(adapters)}")
    adapters.insert(0,0)
    print(f"Task 2: {task_2(adapters)}")

if __name__ == "__main__":
  main()