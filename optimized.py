from tqdm import tqdm
import time
import csv

start_time = time.time()
file_csv = "csv/dataset1_Python+P7.csv"
# file_csv = "csv/dataset2_Python+P7.csv"
# file_csv = "csv/20_shares.csv"
MAX_BUDGET = 500


# lire mon csv et créer une liste de dict
def read_file(path):
    shares = []
    with open(path, mode='r') as csv_file:
        csv_line = csv.DictReader(csv_file)
        for share in csv_line:
            name = share['name']
            price = int(float(share['price']) * 100)
            profit = round((float(share['profit']) / 100) * (float(share['price']) * 100), 2)
            if float(share['price']) > 0:
                share = {"name": name, "price": price, "profit": int(profit)}
            shares.append(share)
    return shares


def knapsack(shares):
    budget = int(MAX_BUDGET * 100)
    all_shares = len(shares)
    matrix = [[0 for x in range(budget + 1)] for x in range(all_shares + 1)]

    for i in tqdm(range(1, all_shares + 1)):
        for j in range(1, budget + 1):
            if shares[i - 1]['price'] <= j:
                matrix[i][j] = max(
                    shares[i - 1]['profit'] + matrix[i - 1][j - shares[i - 1]['price']], matrix[i - 1][j])
            else:
                matrix[i][j] = matrix[i - 1][j]


    n = all_shares
    best_combination = []
    while budget > 0 and n > 0:
        share = shares[n - 1]
        if matrix[n][budget] == matrix[n - 1][budget - share['price'] + share['profit']]:
            best_combination.append(share)
            budget -= share['price']
        n -= 1

    return (matrix[-1][-1] / 100), best_combination


# def result_display(best_combination):
#     total_price = []
#     total_profit = []
#     combination = list(best_combination)
#     # combination.sort(key=lambda share: share['profit'], reverse=True)
#     for share in combination:
#         print(f"{share['name']} | {share['price']} | {share['profit']} €")
#         total_price.append(share['price'] / 100)
#         total_profit.append(share['profit'])
#
#     print(f"\nNombre d'actions à achetés : {len(combination)}")
#     print(f"\nPrix total : ", sum(total_price), "€")
#     # print(f"\nBenefice après 2 ans en pourcentage: {str(total_profit / total_price * 100)[:5]}", "%")
#     print(f"\nBenefice après 2 ans : ", sum(total_profit), "€")
#     print("\nTemps d'éxecution : ", str(time.time() - start_time)[:4], "secondes")


def main():
    shares = read_file(file_csv)
    print(knapsack(shares))
    # best_combination = knapsack(shares)
    # result_display(best_combination)


if __name__ == '__main__':
    main()
