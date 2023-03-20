dict_int = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dict_resultat = {key: value for key, value in dict_int.items() if key > 2 and key < 5}

print(dict_resultat)
