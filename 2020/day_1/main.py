import time as t

# Complexity of O(n^2)
def task_1 (nums) :
  length = len(nums)
  
  for i in range(length) :
    for j in range(i + 1, length) :
      x = nums[i]
      y = nums[j]
      if (x + y == 2020) :
        print (x, " * ", y, " = ", x * y)

# Complexity of O(n^3)
def task_2 (nums) :
  length = len(nums)
  for i in range(length) :
    for j in range(i + 1, length) :
      for k in range(j + 1, length) :
        x = nums[i]
        y = nums[j]
        z = nums[k]
        if (x + y + z == 2020) :
          print (x, " * ", y, " * ", z , " = ", x * y * z)

# Complexity of O(n)
def task_1_fast (nums) :
  d = set()
  for i in nums :
    inv = 2020 - i
    if (inv in d) :
      print(i, " * ", inv, " = ", i * inv)
      return
    d.add(i) 


# Complexity of O(n^2)
def task_2_fast (nums) : 
  length = len(nums)
  d = set()
  for i in range(length) :
    for j in range(i + 1, length) :
        x = nums[i]
        y = nums[j]
        inv = 2020 - x - y

        if (inv in d) :
          print(x, " * ", y, " * ", inv, " = ", x * y * inv)
          return

        d.add(x)
        d.add(y) 

def main () :
  test_nums = [1721, 979, 366, 299, 675, 1456]
  with open("input_day_1.txt", 'r') as input_day_1 :
    input_list = [int(i) for i in input_day_1.read().splitlines() ]

  start_task_1 = t.time()
  task_1(input_list)
  end_task_1 = t.time()

  start_task_fast_1 = t.time()
  task_1_fast(input_list)
  end_task_fast_1 = t.time()
  
  start_task_2 = t.time()
  task_2(input_list)
  end_task_2 = t.time()

  start_task_fast_2 = t.time()
  task_2_fast(input_list)
  end_task_fast_2 = t.time()

  print("Time used to compute task 1:       ", (end_task_1 - start_task_1))
  print("Time used to compute task 1 fast:  ", (end_task_fast_1 - start_task_fast_1))
  print("Time used to compute task 2:       ", (end_task_2 - start_task_2))
  print("Time used to compute task 2 fast: ", (end_task_fast_2 - start_task_fast_2))

if __name__ == "__main__":
    main()