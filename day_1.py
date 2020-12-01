def task_1 (nums) :
  length = len(nums)
  
  for i in range(length) :
    for j in range(i + 1, length) :
      x = nums[i]
      y = nums[j]
      if (x + y == 2020) :
        print (x, " * ", y, " = ", x * y)

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


def main () :
  test_nums = [1721, 979, 366, 299, 675, 1456]
  with open("input_day_1.txt", 'r') as input_day_1 :
    input_list = [int(i) for i in input_day_1.read().splitlines() ]

  task_1(input_list)
  task_2(input_list)

if __name__ == "__main__":
    main()