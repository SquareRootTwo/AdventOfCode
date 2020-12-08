import re

def execute(insn, n) :
  count = 0
  visited = [False] * n
  ins_ptr = 0
  while ins_ptr < n :
    ins, amnt = insn[ins_ptr]
    if visited[ins_ptr] :
      return count
    visited[ins_ptr] = True
    if (ins == "acc") :
      count += amnt
      ins_ptr += 1
    elif (ins == "jmp") :
      ins_ptr += amnt
    else :
      ins_ptr += 1
  return count

def returns(insn, n) :
  count = 0
  visited = [False] * n
  ins_ptr = 0
  while ins_ptr < n :
    ins, amnt = insn[ins_ptr]
    if visited[ins_ptr] :
      return False
    visited[ins_ptr] = True
    if (ins == "acc") :
      count += amnt
      ins_ptr += 1
    elif (ins == "jmp") :
      ins_ptr += amnt
    else :
      ins_ptr += 1
  return True

def task_2(insn, n) :
  for i in range(n) :
    ins, amnt = insn[i]
    if ins == "jmp" :
      insn[i] = "nop", amnt
      if (returns(insn, n)) :
        return execute(insn, n)
      else :
        insn[i] = "jmp", amnt
    elif ins == "nop" :
      insn[i] = "jmp", amnt
      if (returns(insn, n)) :
        return execute(insn, n)
      else :
        insn[i] = "nop", amnt
  return -1

def main() :
  with open("input_day_8.txt", 'r') as input_file :
    insn = [(re.findall("[a-z]{3}", line)[0], int(re.findall("\+[0-9]+|-[0-9]+", line)[0])) for line in input_file ]
    n = len(insn)
  print(f"Task 1: {execute(insn, n)}")
  print(f"Task 2: {task_2(insn, n)}")

if __name__ == "__main__":
  main()