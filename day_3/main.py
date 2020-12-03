import functools as fun
import numpy as np
import operator as op

def task_1(trees, y_max, x_max, slope_x, slope_y) :
  encountered_trees = 0
  x_offset = 0
  for h in range(0, y_max, slope_y) :
    encountered_trees += trees[h][x_offset % x_max]
    x_offset += slope_x

  return encountered_trees

def task_2(trees, y_max, x_max) :
  slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
  encountered_trees = []
  for s in slopes :
    slope_x = s[0]
    slope_y = s[1]
    encountered_trees.append(task_1(trees, y_max, x_max, slope_x, slope_y))

  return fun.reduce(op.mul, encountered_trees)
  # return slopes[np.argmin(encountered_trees)]

def main() :
  n = len(open("input_day_3.txt").readlines())
  m = len(open("input_day_3.txt").readline()) - 1
  with open("input_day_3.txt", 'r') as input_day_3 :
    P = lambda x : 1 if (x == "#") else 0
    trees = [[P(line[j]) for j in range(m)] for line in input_day_3]

  slope_x = 3
  slope_y = 1
  encountered_trees = task_1(trees, n, m, slope_x, slope_y)
  print("Task 1: \n")
  print("Grid dim: {}, {}".format(n, m))
  print("Encountered trees: {}".format(encountered_trees))

  mult_encountered_trees = task_2(trees, n, m)
  print("Task 2: \n")
  print("Best strategy: {}".format(mult_encountered_trees))


if __name__ == "__main__":
  main()

