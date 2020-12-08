import System.Environment
import Data.List
import Parsec


data Ins = Nop | Jmp a | Acc a

parse_input :: String -> [Ins]
parse (x:y:z:ls)
  | (x1:x2:x3:space:sign:) == "jmp" =
  | (x1:x2:x3:space:sign:) == "nop" =
  | (x1:x2:x3:space:sign:) == "acc" = 
  | (x:y) == "\n" = parse_input (z:ls)
  | [] = []
  | _ = parse_input (y:z:ls)

parse_input (x:xs) 
  | 

main = do 
  f <- readFile "input_day_8.txt"

