# import comb (combinations) function from math library
from math import comb
# open the .txt file and extract data from it.
with open("/Users/ASHRAF/Desktop/Rosalind/rosalind_lia_1_dataset.txt") as Data_file:
    Data = Data_file.readline().strip()
k, n = map(int, Data.split(" "))
# this CDF function below will calculate The probability that at least N AaBb organisms will belong
# to the k-th generation of Tom's family tree
def CDF_binomial_dis(k,n):
    prob = []
    num = 2 ** k
    for i in range(1, n):
        prob.append(comb(num,i)* 0.25**i * 0.75**(num-i))
    return 1 - sum(prob)
print("The probability that at least N AaBb organisms will belong to the k-th generation of Tom's family tree is:",
      round(CDF_binomial_dis(k, n), 6))
