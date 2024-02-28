# import urllib library, we will meed it to connect with uniprot database website and extract protein strings from it.
import urllib.request
# open the .txt file and extract data from it.
with open("/Users/ASHRAF/Desktop/Rosalind/rosalind_mprt.txt") as Data_file:
    Data = Data_file.readlines()
# extract uniprot IDs from the data file
uniprot_IDs = dict()
given_uni_IDs = dict()
for line in Data:
    if "_" in line:
        ID_end = line.find("_")
        uniprot_IDs[line[: ID_end]] = ""
        given_uni_IDs[line[: ID_end]] = line.strip()
    else:
        uniprot_IDs[line.strip()] = ""
        given_uni_IDs[line.strip()] = line.strip()
print(uniprot_IDs.keys())
# upload the protein sequences from uniprot database website to the IDs dictionary
# note: this step needs intrnet!
for ID in uniprot_IDs.keys():
    fasta = urllib.request.urlopen("http://www.uniprot.org/uniprot/" + ID + ".fasta").readlines()
    prot_seq = ""
    for line in range(1, len(fasta)):
        prot_seq += str(fasta[line]).strip()[2: -3]
    uniprot_IDs[ID] = prot_seq
# searching for N-glycosylation motif locations in every protein sequence and print them out
print("Access ID for pretein sequences that contain N-glycosylation motif and locations of these motifs are:")
for ID in uniprot_IDs.keys():
    N_glyco_locations = list()
    for aa in range(len(uniprot_IDs[ID]) - 3):
        motif = uniprot_IDs[ID][aa: aa+4]
        if motif[0] == "N":
            if motif[1] != "P" and motif[3] != "P":
                if motif[2] == "S" or motif[2] == "T":
                    N_glyco_locations.append(aa + 1)
    if len(N_glyco_locations) != 0:
        print(given_uni_IDs[ID])
        print(*N_glyco_locations)
