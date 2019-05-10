import csv

count = 0

filepath = '/Users/user1/Desktop/WSJ/\\17_4_2019\\AMEX.csv'


with open(filepath, 'r') as csvFile:
    r = csv.reader(csvFile)
    ir = iter(r)
    next(ir)
    for row in ir:
        sym = row[1]
        if '%' in sym:
            continue
        if '.' in sym:
            continue
        count += 1

print(count)


csvFile.close()