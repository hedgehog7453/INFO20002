import pandas as pd
import csv

FILENAME = "assets/dataset.csv"
ORIGINAL_COL = ["Date Of Stop", 
                "Month Of Stop",
                "Year Of Stop",
                "Time Of Stop", 
                "Time Period",
                "Description", 
                "Belts", 
                "Personal Injury", 
                "Commercial License", 
                "Commercial Vehicle", 
                "Vehicle Type", 
                "Year", 
                "Make", 
                "Model", 
                "Color", 
                "Race", 
                "Gender"]
TRIMMED_COL = map(lambda x: x.replace(" ", "").lower(), ORIGINAL_COL)


'''
Read dataset.csv
Return a 2D list of data, with the first row as column names. 
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
From trimmed column name (or list of column names) to original column name,
or the other way around
'''
def t2o2t(attr):
    if type(attr) is list:
        l = ORIGINAL_COL if attrs == TRIMMED_COL else TRIMMED_COL
        return l
    else:
        try: return ORIGINAL_COL[TRIMMED_COL.index(attr)]
        except ValueError: return TRIMMED_COL[ORIGINAL_COL.index(attr)]


'''
Takes a DataFrame object and filter it by the input condition. 
Return the DataFrame object after filtering. 
'''
def filter_df(df, filter_attr, filter_cond, filter_val):
    bools = []
    if filter_cond=="yes" or filter_cond=="no":
        bools = []
    elif filter_cond=="contains" or filter_cond=="notContain":
        bools = []
    else:
        bools = []
    return df


'''

'''
def pivot_table_builder_func(row, col, aggr_m, aggr_a, filter_attr, filter_cond, filter_val):
    odf = pd.read_csv(FILENAME)
    if not filter_cond=="none":
        df = filter_df(odf, filter_attr, filter_cond, filter_val)
    else:
        df = odf
    t = pd.pivot_table(df, index = [row], columns = [col], values = [aggr_a], aggfunc={aggr_a:len})

    return t









