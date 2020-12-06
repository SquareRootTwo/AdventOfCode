import re

def task_1() :
  with open("input_day_6.txt", 'r') as input_file :
    line = input_file.readline()
    count = 0
    while line : 
      group = set()

      while line and line != "\n" :
        l = line.rstrip()
        nr_questions = len(l)
        for i in range(nr_questions) :
          group.add(line[i])
        line = input_file.readline()
      line = input_file.readline()
      count += len(group)
    print(f"Total answered question: {count}")
  return count

def task_2() :
  with open("input_day_6.txt", 'r') as input_file :
    line = input_file.readline()
    count = 0
    while line : 
      group = []
      while line and line != "\n" :
        l = line.rstrip()
        nr_questions = len(l)
        group_member = set()

        for i in range(nr_questions) :
          group_member.add(line[i])
        line = input_file.readline()
        group.append(group_member)

      ans_fst = group[0]
      group_size = len(group)
      group_count = 0
      for ans in ans_fst :
        ans_count = 0
        for i in group :
          if (ans in i) :
            ans_count += 1
        if (ans_count == group_size) :
          group_count += 1

      count += group_count

      line = input_file.readline()
    print(f"Total answered question by all group members: {count}")
  return count
  return 1

def main() : 
  task_1()
  task_2()



if __name__ == "__main__":
  main()