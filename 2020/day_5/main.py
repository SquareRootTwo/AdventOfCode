def get_row_nr(enc_nr) :
  l = len(enc_nr)
  nr = 0
  for i in range(l) :
    if (enc_nr[i] == "B") :
      nr += 2**(6-i)
  return nr

def get_col_nr(enc_nr) :
  l = len(enc_nr)
  nr = 0
  for i in range(l) :
    if (enc_nr[i] == "R") :
      nr += 2**(2-i)
  return nr

def get_seat_id(enc_nr) :
  row_enc_nr = enc_nr[:7]
  col_enc_nr = enc_nr[7:]
  row_nr = get_row_nr(row_enc_nr)
  col_nr = get_col_nr(col_enc_nr)
  
  return (8 * row_nr) + col_nr

def get_seat_ids() : 
  seat_ids = []
  with open("input_day_5.txt", 'r') as input_file :
    for line in input_file :
      seat_id = get_seat_id(line)
      seat_ids.append(seat_id)

  return seat_ids

def task_1() :
  seat_ids = get_seat_ids()
  max_id = max(seat_ids)
  # print(max_id)
  return max_id

def task_2() :
  max_seat_id = task_1()
  seat_set_ids = set(get_seat_ids())
  for i in range(1, max_seat_id) :
    if ((i - 1) in seat_set_ids) and not (i in seat_set_ids) and ((i + 1) in seat_set_ids) : 
      print(f"Your seat id: {i}")
      return i
      break 
  return -1


def main() :
  # print(get_seat_id("FBFBBFFRLR"))
  task_2()


if __name__ == "__main__":
  main()