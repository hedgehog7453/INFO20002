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
# Trimmed column names that are used as IDs in html tags
TRIMMED_COL = map(lambda x: x.replace(" ", "").lower(), ORIGINAL_COL)


'''
Read dataset.csv and return a 2D list of data, with the first row as column 
names. 
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
From trimmed column name (or list of column names) to original column name (or 
list of original column names), or the other way around. 
'''
def t2o2t(attr):
    if type(attr) is list:
        l = ORIGINAL_COL if attrs == TRIMMED_COL else TRIMMED_COL
        return l
    else:
        try: return ORIGINAL_COL[TRIMMED_COL.index(attr)]
        except ValueError: return TRIMMED_COL[ORIGINAL_COL.index(attr)]


'''
Take a DataFrame object and filter it by the input condition.
Return the DataFrame object after filtering. 
'''
def filter_df(df, filter_attr, filter_cond, filter_val):
    if filter_cond=="none":
        return df
    else:
        bools = []
        if filter_cond=="=":
            for cell in df[str(filter_attr)]:
                if cell==filter_val: bools.append(True)
                else: bools.append(False)
        elif filter_cond==">":
            for cell in df[str(filter_attr)]:
                if int(cell)>int(filter_val): bools.append(True)
                else: bools.append(False)
        elif filter_cond=="<":
            for cell in df[str(filter_attr)]:
                if int(cell)<int(filter_val): bools.append(True)
                else: bools.append(False)
        elif filter_cond=="!=":
            for cell in df[str(filter_attr)]:
                if cell!=filter_val: bools.append(True)
                else: bools.append(False)
        elif filter_cond=="contains":
            for cell in df[str(filter_attr)]:
                if filter_val in cell: bools.append(True)
                else: bools.append(False)
        elif filter_cond=="notContain":
            for cell in df[str(filter_attr)]:
                if filter_val in cell: bools.append(False)
                else: bools.append(True)
        elif filter_cond=="yes":
            for cell in df[str(filter_attr)]:
                if cell=="Yes": bools.append(True)
                else: bools.append(False)
        elif filter_cond=="no":
            for cell in df[str(filter_attr)]:
                if cell=="No": bools.append(True)
                else: bools.append(False)
        series = pd.Series(bools)
        return df[series]

'''
Build the pivot table and return a panda DataFrame object. 
'''
def pivot_table_builder_func(row, col, aggr_m, aggr_a, filter_attr, filter_cond, filter_val):
    odf = pd.read_csv(FILENAME)
    df = filter_df(odf, filter_attr, filter_cond, filter_val)
    t = pd.pivot_table(df, index = [row], columns = [col], values = [aggr_a], aggfunc={aggr_a:len})

    return t









