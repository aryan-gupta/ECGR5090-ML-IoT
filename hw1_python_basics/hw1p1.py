#!/usr/bin/env python

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))
  

list_of_name_len = [len(x) for x in list_of_names]

for i in range(len(list_of_names)):
  print(f"{list_of_names[i]} :: {list_of_name_len[i]}")