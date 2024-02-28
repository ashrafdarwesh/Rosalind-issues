
# open the .txt file and extract data from it.
with open("/Users/HASAN/Desktop/Rosalind/rosalind_grph_1_dataset.txt") as Data_file:
    Data = Data_file.readlines()
# format the FASTA data in a tidy and readable form (I chose to format them in a dictionary in this case)
num_of_fragment = 0
dict_of_fragments = dict()
for line in range(len(Data)):
    if Data[line].startswith(">"):
        num_of_fragment += 1
        ID = Data[line][1:].strip()
        dict_of_fragments[ID] = ""
    else:
        dict_of_fragments[ID] += Data[line].strip()
# now I will print the number of DNA fragments and the first 5 DNA fragments and their rosalind IDs
print("The number of DNA fragments:", num_of_fragment)
first_5_keys = list(dict_of_fragments.keys())[: 5]
print("The first 5 DNA fragments and IDs are:")
for key in first_5_keys:
    print(key, dict_of_fragments[key])
    # this function will determine the rosalind IDs of DNA sequences which overlap by 3 nucleotides
def overlap(ID_dict):
    for ID_1 in ID_dict.keys():
        for ID_2 in ID_dict.keys():
            if ID_dict[ID_1][-3:] == ID_dict[ID_2][0: 3]:
                if ID_dict[ID_1] != ID_dict[ID_2]:
                    print(ID_1, ID_2)
print("Rosalind IDs list of the overlaped DNA strings by 3 nucleotides are:")
overlap(dict_of_fragments)