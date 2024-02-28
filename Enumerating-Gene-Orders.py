# import important libraries
from math import perm
from itertools import permutations 
# open the .txt file and extract data from it.
with open("/Users/ASHRAF/Desktop/Rosalind/rosalind_perm_1_dataset.txt") as Data_file:
    Data = Data_file.readline().strip()
set_size = int(Data)
print("The size of the set is:", set_size)

# I added one to the set size cause the range function doesn't include the last element in the list
set_elements = list(range(1, set_size + 1))
print("The elements of the set are:", set(set_elements))
print("The total number of possible permutations of length {} is:".format(set_size), perm(set_size, set_size))
print("All of the unique permutations sets are:")
print(*list(permutations(set_elements)))
