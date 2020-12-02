import re

def task_1 (pw, char, min_occ, max_occ) :
  count_valid_pws = 0
  n = len(pw)
  for i in range(n) : 
    char_i_occurrence = pw[i].count(char[i])
    
    if (char_i_occurrence >= min_occ[i]) and (char_i_occurrence <= max_occ[i]) :
      count_valid_pws += 1
  
  print("Task 1: ", count_valid_pws)

def task_2 (pw, char, min_loc, max_loc) : 
  count_valid_pws = 0
  n = len(pw)
  for i in range(n) :
    pw_len = len(pw[i]) 
    min_pos = min_loc[i] - 1
    max_pos = max_loc[i] - 1
    if (min_pos >= 0 and max_pos < pw_len and ((char[i] == pw[i][min_pos]) ^ (char[i] == pw[i][max_pos]))) : 
      count_valid_pws += 1
  
  print("Task 2: ", count_valid_pws)

def main () :
  pattern = '\d+-\d+\s*[a-z]:\s*[a-z]*$'
  min_occ = []
  max_occ = []
  char = []
  pw = []

  with open("input_day_2.txt", 'r') as input_day_2 :
    for line in input_day_2 : 
      max_min_char = re.findall("\d+", line)
      char_pw = re.findall("[a-z]+", line)
      min_occ.append(int(max_min_char[0]))
      max_occ.append(int(max_min_char[1]))
      char.append(char_pw[0])
      pw.append(char_pw[1])

  task_1(pw, char, min_occ, max_occ)
  task_2(pw, char, min_occ, max_occ)

if __name__ == "__main__":
  main()