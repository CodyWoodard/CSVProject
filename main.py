# Familiarizing myself with csv.reader in Python. Received this from
# Pythons docs @ https://docs.python.org/3/library/csv.html
if __name__ == '__main__':

    import csv
    with open('BobsParts.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in spamreader:
            print(', '.join(row))



