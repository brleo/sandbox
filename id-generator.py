import csv

file = "common/csv/DJ"
header = ["id","firstName","lastName","gender","country"]

with open(file + ".csv") as inp, open(file + "_ID.csv", 'w') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out, delimiter=',')
    writer.writerow(header)
    writer.writerows([i] + row for i, row in enumerate(reader, 1))