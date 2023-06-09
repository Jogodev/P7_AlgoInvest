import time
import psutil
from tqdm import tqdm

import csv

start_time = time.time()
# file_csv = "csv/dataset1_Python+P7.csv"
# file_csv = "csv/dataset2_Python+P7.csv"
file_csv = "csv/20_shares.csv"
MAX_BUDGET = 500


# lire mon csv et créer une liste de dict
def read_file(path):
    shares = []
    with open(path, mode='r') as csv_file:
        csv_line = csv.DictReader(csv_file)
        for share in csv_line:
            if float(share['price']) > 0 and float(share['profit']) > 0:
                name = share['name']
                price = int(float(share['price']) * 100)
                profit = int((float(share['profit']) / 100) * (float(share['price']) * 100))
                share = {"name": name, "price": price, "profit": profit}
                shares.append(share)
    return shares


def knapsack(shares):
    budget = int(MAX_BUDGET * 100)
    matrix = [[0 for x in range(budget + 1)] for x in range(len(shares) + 1)]
    for i in tqdm(range(1, len(shares) + 1)):
        for j in range(1, budget + 1):
            if shares[i - 1]['price'] <= j:
                matrix[i][j] = max(
                    shares[i - 1]['profit'] + matrix[i - 1][j - shares[i - 1]['price']], matrix[i - 1][j])
            else:
                matrix[i][j] = matrix[i - 1][j]
    n = len(shares)
    best_combination = []
    while budget > 0 and n > 0:
        share = shares[n - 1]
        if matrix[n][budget] == matrix[n - 1][budget - share['price']] + share['profit']:
            best_combination.append(share)
            budget -= share['price']
        n -= 1

    total_price = sum([share['price'] for share in best_combination])
    return [(matrix[-1][-1] / 100), total_price, best_combination]


def result_display(best_combinations):
    total_profit = best_combinations[0]
    total_price = best_combinations[1]
    combination = list(best_combinations[2])
    combination.sort(key=lambda share: share['profit'], reverse=True)
    for share in combination:
        print(f"{share['name']} | {share['price'] / 100} | {share['profit'] / 100} €")

    print(f"\nNombre d'actions à achetés : {len(combination)}")
    print(f"\nPrix total : {total_price / 100}", "€")
    print(f"\nBenefice après 2 ans en pourcentage: {str((total_profit / total_price * 100) * 100)[:5]}", "%")
    print(f"\nBenefice après 2 ans : {total_profit}", "€")
    print("\nTemps d'éxecution : ", str(time.time() - start_time)[:4], "secondes")
    print(f"\nMémoire utilisé : {psutil.Process().memory_info().rss / 1024 ** 2}", "MB")


def main():
    shares = read_file(file_csv)
    best_combination = knapsack(shares)
    result_display(best_combination)


if __name__ == '__main__':
    main()
