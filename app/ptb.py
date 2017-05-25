import pandas as pd
import csv

FILENAME = "assets/dataset.csv"


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


'''

'''
def pivot_table_builder_func(row, col, aggr_m, aggr_a):
	df = pd.read_csv(FILENAME)

	t = pd.pivot_table(df, index = [row], columns = [col], values = [aggr_a], aggfunc={aggr_a:len})

	return t









