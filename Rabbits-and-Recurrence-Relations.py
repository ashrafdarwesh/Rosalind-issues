
Rabbits and Recurrence Relations
This is the fourth problem in rosalind bioinformatics stronghold list
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# open the .txt file and extract data from it.
with open("/Users/HASAN/Desktop/Rosalind/rosalind_fib_1_dataset.txt") as Data_file:
    Data = list(map(int, Data_file.readline().strip().split(" ")))
n = int(Data[0])  # n is the number of months
k = int(Data[1])  # k is the number of rabbit pairs produced by each rabbit pair
print(n, k)
35 4
# calculate the total number of rabbit pairs after n months
def FIBO_rab(n, k):
    num_of_pairs_per_month = [1, 1]
    for month in range(n - 2):
        num_of_pairs_per_month.append(num_of_pairs_per_month[month + 1] + k * num_of_pairs_per_month[month])
        # what we care about in this problem is the total number of rabbit pairs so we take the last number in the list
    return num_of_pairs_per_month[-1]  
print("The total number of rabbit pairs after n months is:", FIBO_rab(n, k))