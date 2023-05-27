from tqdm import tqdm
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


def knapsack(shares):
    matrix = [[0 for x in range(max_budget + 1)] for x in range(len(shares) + 1)]

    for share in tqdm(range(1, len(shares) + 1)):
        for w in range(1, max_budget + 1):
            if shares[share - 1]['w'] <= w:
                matrix[share][w] = max(shares[share - 1]['profit'] + matrix[share - 1][w - shares[share - 1]], matrix[share - 1][w])

