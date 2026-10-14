(* Advent of Code 2020, jour 2.
   Chaque ligne est lue avec Scanf.bscanf et le format "%d-%d %c: %s".
   Partie 1 : nombre d'occurrences du caractère entre i et j (fonction
   récursive compte_occ). Partie 2 : ou exclusif entre deux positions. *)

let lit_entree ib =
  Scanf.bscanf ib "%d-%d %c: %s\n"
    (fun i j c password -> (* la fonction à appliquer sur ce qu'on a lu *)
      (i, j, c, password))

let rec lit_tout ib =
  try
    let e = lit_entree ib in
    (* petite subtilité : OCaml évalue de droite à gauche, donc si on
       écrivait directement lit_entree ib :: lit_tout ib, l'appel récursif
       serait fait en premier et ne terminerait pas *)
    e :: lit_tout ib (* on lit une entrée et on passe à la suite *)
  with End_of_file -> [] (* on arrive ici quand on a lu tout le fichier *)

let rec compte_occ s c i =
  if i >= String.length s
  then 0
  else (if s.[i] = c then 1 else 0) + compte_occ s c (i+1)

let valide1 (i, j, c, password) =
  let compte = compte_occ password c 0 in
  compte >= i && compte <= j

let valide2 (i, j, c, password) =
  let ci = password.[i-1] = c in
  let cj = password.[j-1] = c in
  (ci && not cj) || (cj && not ci)

let rec compte_l l valide =
  match l with
  | [] -> 0
  | e :: q -> (if valide e then 1 else 0) + compte_l q valide

let _ =
  let ic = open_in "day2020_02.txt" in
  let ib = Scanf.Scanning.from_channel ic in
  let l = lit_tout ib in
  Printf.printf "Partie 1 : %d\nPartie 2 : %d\n"
    (compte_l l valide1)
    (compte_l l valide2)
