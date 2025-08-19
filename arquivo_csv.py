import csv

with open('seuarquivo.csv') as f:
    for linha in csv.reader(f):
        print(linha)
