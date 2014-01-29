let read_int () = int_of_string (input_line stdin);;
let n = read_int ();;
let rec stair n =
    if n = 0 then [] else read_int () :: stair (n - 1);;
let rec expected_value l = match l with
    | [] -> 0.0
    | h :: t -> 0.5 *. (float_of_int h) +. (expected_value t);;
Printf.printf "%0.1f" (expected_value (stair n));;