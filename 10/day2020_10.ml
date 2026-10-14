(* Advent of Code 2020, jour 10.
   Partie 1 : après tri, on compte les écarts de 1 et de 3 entre voisins.
   Partie 2 : dénombrement des chaînes de haut en bas, mémoïsé dans un
   tableau d'options : count prev est le nombre de façons de finir la chaîne
   depuis l'adaptateur prev (l'indice n représente la prise, de valeur 0). *)

let adapteurs =
  let ic = open_in "day2020_10.txt" in
  let rec lit acc =
    match input_line ic with
    | l -> lit (int_of_string (String.trim l) :: acc)
    | exception End_of_file -> close_in ic; Array.of_list (List.rev acc)
  in lit []

let partie1 () =
  Array.sort compare adapteurs;
  let compte1 = ref 0 in
  let compte3 = ref 1 in (* le dernier écart, vers l'appareil, vaut 3 *)
  for i = 0 to Array.length adapteurs - 1 do
    let precedent = if i = 0 then 0 else adapteurs.(i-1) in
    let ecart = adapteurs.(i) - precedent in
    if ecart = 1 then incr compte1;
    if ecart = 3 then incr compte3
  done;
  !compte1 * !compte3

let partie2 () =
  Array.sort compare adapteurs;
  let n = Array.length adapteurs in
  let cache = Array.make (n+1) None in
  let rec count prev =
    match cache.(prev) with
    | None ->
      let c = ref 0 in
      let suivant, vprev = if prev = n then 0, 0 else prev+1, adapteurs.(prev) in
      let feuille = ref true in
      (* les successeurs possibles sont parmi les trois adaptateurs suivants *)
      for i = suivant to min (n-1) (suivant+2) do
        let v = adapteurs.(i) in
        if v - vprev <= 3
        then begin
          c := !c + count i;
          feuille := false
        end
      done;
      let v = if !feuille then 1 else !c in
      cache.(prev) <- Some v;
      v
    | Some v -> v
  in
  count n

let _ =
  Printf.printf "Partie 1 : %d\nPartie 2 : %d\n" (partie1 ()) (partie2 ())
