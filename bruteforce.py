from itertools import combinations
import time
import csv

start_time = time.time()

file_csv = "csv/20_actions.csv"
max_budget = 500


# lire mon csv et créer une liste de dict
def read_file(path):
    actions = []
    with open(path, mode='r') as csv_file:
        csv_line = csv.DictReader(csv_file)
        for action in csv_line:
            action['price'] = float(action['price'])
            action['profit'] = (action['price'] * float(action['profit']) / 100)
            actions.append(action)
    return actions


# Créer la liste de toutes les combinaisons
def get_best_combinations(actions):
    best_profit = 0
    best_combination = []
    for action in range(len(actions)):
        for combination in combinations(actions, action):
            total_price = sum([action['price'] for action in combination])
            if total_price <= max_budget:
                total_profit = sum(action['profit'] for action in combination)
                if total_profit > best_profit:
                    best_combination = [total_price, total_profit, combination]
    return best_combination


def result_display(best_combinations):
    total_price = best_combinations[0]
    total_profit = best_combinations[1]
    combination = list(best_combinations[2])
    combination.sort(key=lambda action: action['profit'], reverse=True)
    for action in combination:
        print(f"{action['name']} | {action['price']} | {action['profit']} €")

    print(f"\nPrix total : {total_price}", "€")
    print(f"\nBenefice après 2 ans : {total_profit}", "€")
    print("\nTemps d'éxecution : ", time.time() - start_time, "secondes")


def main():
    actions = read_file(file_csv)
    best_combination = get_best_combinations(actions)
    result_display(best_combination)


if __name__ == '__main__':
    main()
