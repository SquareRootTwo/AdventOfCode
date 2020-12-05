import re

def check_pp(curr_pp, valid_pp) : 
  if  ((curr_pp['byr'] == None) or 
      (curr_pp['iyr'] == None) or
      (curr_pp['eyr'] == None) or
      (curr_pp['hgt'] == None) or
      (curr_pp['hcl'] == None) or
      (curr_pp['ecl'] == None) or
      (curr_pp['pid'] == None)) :
    return 0
  else : 
    (valid_pp.append(curr_pp))
    return 1

def check_2_pp(curr_pp, valid_pp) : 
  byr_p = "(19[2-9][0-9])|(200[0-2])" 
  iyr_p = "(201[0-9])|(2020)"
  eyr_p = "(202[0-9])|(2030)"
  hgt_p = "(((15[0-9])|(16[0-9])|(17[0-9])|(18[0-9])|(19[0-3]))cm)|(((59)|(6[0-9])|(7[0-6]))in)" 
  hcl_p = "#[0-9a-f]{6}"
  ecl_p = "(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)"
  pid_p = "[0-9]{9}"
  if  ((curr_pp['byr'] == None) or 
      (curr_pp['iyr'] == None) or
      (curr_pp['eyr'] == None) or
      (curr_pp['hgt'] == None) or
      (curr_pp['hcl'] == None) or
      (curr_pp['ecl'] == None) or
      (curr_pp['pid'] == None)) :  
    return 0
  else : 
    if (
      re.match(byr_p, curr_pp['byr']) and
      re.match(iyr_p, curr_pp['iyr']) and
      re.match(eyr_p, curr_pp['eyr']) and
      re.match(hgt_p, curr_pp['hgt']) and
      re.match(hcl_p, curr_pp['hcl']) and
      re.match(ecl_p, curr_pp['ecl']) and
      re.match(pid_p, curr_pp['pid'])
    ) :
      valid_pp.append(curr_pp)
      print(curr_pp)
      return 1
    else :
      return 0

def task_1() :
  pps = []
  valid_pp = []

  # parse input file
  with open("input_day_4.txt", 'r') as input_file :
    curr_pp = {}
    pair = "[a-z]+:[a-zA-Z0-9#]+"
    field = "[a-z]+:"
    value = ":[a-zA-Z0-9#]+"

    curr_pp['byr'] = None
    curr_pp['iyr'] = None
    curr_pp['eyr'] = None
    curr_pp['hgt'] = None
    curr_pp['hcl'] = None
    curr_pp['ecl'] = None
    curr_pp['pid'] = None
    curr_pp['cid'] = None
    count_valid = 0
    count_all = 0
    for line in input_file : 
      # print(line)
      if (line != "\n") : 
        pairs = re.findall(pair, line)
        for p in pairs :
          v = re.findall(value, p)[0].strip(":")
          f = (re.findall(field, p))[0].strip(":")
          curr_pp[f] = v
      else : 
        pps.append(curr_pp)
        check_pp(curr_pp, valid_pp)
        count_all += 1
        # print(f"append item: {curr_pp}")
        curr_pp = dict()
        curr_pp['byr'] = None
        curr_pp['iyr'] = None
        curr_pp['eyr'] = None
        curr_pp['hgt'] = None
        curr_pp['hcl'] = None
        curr_pp['ecl'] = None
        curr_pp['pid'] = None
        curr_pp['cid'] = None

    pps.append(curr_pp)
    check_pp(curr_pp, valid_pp)
    print(f"Valid pps: {len(valid_pp)}")
    print(f"All pps: {count_all}")
  return len(valid_pp)

def task_2() : 
  pps = []
  valid_pp = []

  # parse input file
  with open("input_day_4.txt", 'r') as input_file :
    curr_pp = {}
    pair = "[a-z]+:[a-zA-Z0-9#]+"
    field = "[a-z]+:"
    value = ":[a-zA-Z0-9#]+"

    curr_pp['byr'] = None
    curr_pp['iyr'] = None
    curr_pp['eyr'] = None
    curr_pp['hgt'] = None
    curr_pp['hcl'] = None
    curr_pp['ecl'] = None
    curr_pp['pid'] = None
    curr_pp['cid'] = None
    count_valid = 0
    count_all = 0
    for line in input_file : 
      # print(line)
      if (line != "\n") : 
        pairs = re.findall(pair, line)
        for p in pairs :
          v = re.findall(value, p)[0].strip(":")
          f = (re.findall(field, p))[0].strip(":")
          curr_pp[f] = v
      else : 
        pps.append(curr_pp)
        check_2_pp(curr_pp, valid_pp)
        count_all += 1
        curr_pp = dict()
        curr_pp['byr'] = None
        curr_pp['iyr'] = None
        curr_pp['eyr'] = None
        curr_pp['hgt'] = None
        curr_pp['hcl'] = None
        curr_pp['ecl'] = None
        curr_pp['pid'] = None
        curr_pp['cid'] = None

    pps.append(curr_pp)
    check_2_pp(curr_pp, valid_pp)

    print(f"Valid pps: {len(valid_pp)}")
    # print(f"All pps: {count_all}")
    return len(valid_pp)

def main() : 
  # task_1()
  task_2()

if __name__ == "__main__":
  main()
     