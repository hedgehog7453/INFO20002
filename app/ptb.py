FILENAME = "assets/dataset.csv"
import csv

'''
Read dataset.csv
Return a 2D list of data.
'''
def readcsv():
    f = open(FILENAME)
    csvreader = csv.reader(f, delimiter=',', skipinitialspace=True)
    data = []
    for row in csvreader:
        data.append(row)
    f.close()
    return data

