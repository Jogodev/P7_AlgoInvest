from itertools import combinations
from tqdm import tqdm
import psutil
import time
import csv

start_time = time.time()

file_csv = "csv/20_shares.csv"
max_budget = 500


# lire mon csv et créer une liste de dict
def read_file(path):
    shares = []
    with open(path, mode='r') as csv_file:
        csv_line = csv.DictReader(csv_file)
        for share in csv_line:
            share['price'] = float(share['price'])
            share['profit'] = (share['price'] * float(share['profit']) / 100)
            shares.append(share)
    return shares


# Créer la liste de toutes les combinaisons
def get_best_combinations(shares):
    best_profit = 0
    best_combination = []
    for share in tqdm(range(len(shares))):
        for combination in combinations(shares, share):
            total_price = sum([share['price'] for share in combination])
            if total_price <= max_budget:
                total_profit = sum(share['profit'] for share in combination)
                if total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = [total_price, total_profit, combination]
    return best_combination


def result_display(best_combinations):
    total_price = best_combinations[0]
    total_profit = best_combinations[1]
    combination = list(best_combinations[2])
    combination.sort(key=lambda share: share['profit'], reverse=True)
    for share in combination:
        print(f"{share['name']} | {share['price']} | {share['profit']} €")

    print(f"\nNombre d'actions à achetés : {len(combination)}")
    print(f"\nPrix total : {total_price}", "€")
    print(f"\nBenefice après 2 ans en pourcentage: {str(total_profit / total_price * 100)[:5]}", "%")
    print(f"\nBenefice après 2 ans : {str(total_profit)[:5]}", "€")
    print("\nTemps d'éxecution : ", str(time.time() - start_time)[:4], "secondes")
    print(f"\nMémoire utilisé : {round(psutil.Process().memory_info().rss / 1024 ** 2, 4)}", "MB")


def main():
    shares = read_file(file_csv)
    best_combination = get_best_combinations(shares)
    result_display(best_combination)


if __name__ == '__main__':
    main()