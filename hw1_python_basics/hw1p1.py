#!/usr/bin/env python

import numpy as np

import person

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))
  

list_of_name_len = [len(x) for x in list_of_names]

for i in range(len(list_of_names)):
  print(f"{list_of_names[i]} :: {list_of_name_len[i]}")

people = {}
for i in range(len(list_of_names)):
  people[list_of_names[i]] = person.person(
    name   = list_of_names[i] 
    ,age   =  list_of_ages[i]
    ,height=  list_of_ages[i]
  )

array_of_ages  = np.array(list_of_ages)
array_of_heights_cm = np.array(list_of_heights_cm)

ages_mean = np.mean(array_of_ages)
print(f"The average age is: {ages_mean}")
heights_mean = np.mean(array_of_heights_cm)
print(f"The average height is: {heights_mean}")