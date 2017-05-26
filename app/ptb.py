import pandas as pd
import csv
from math import ceil

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
TRIMMED_COL = list(map(lambda x: x.replace(" ", "").lower(), ORIGINAL_COL))


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
    if aggr_m == "max":
        t = pd.pivot_table(df, index = [row], columns = [col], values = [aggr_a], aggfunc={aggr_a:max})
    elif aggr_m == "min":
        t = pd.pivot_table(df, index = [row], columns = [col], values = [aggr_a], aggfunc={aggr_a:min})
    elif aggr_m == "count":
        t = pd.pivot_table(df, index = [row], columns = [col], values = [aggr_a], aggfunc={aggr_a:len})

    return t


'''
Takes all column values and aggregation values, return a html string
'''
def add_style(row, aggr):
    tbody = ""
    # Find the maximum value and the minimum value (other than 0) from 
    # aggregation values
    max_val = 0
    min_val = aggr[0][0]
    for r in aggr:
        for cell in r:
            if cell>max_val: max_val=cell
            if cell<min_val and cell!=0: min_val=cell
    # Find the corresponding color for each cell
    r_max = 227
    g_max = 74
    b_max = 51
    r_min = 254
    g_min = 232
    b_min = 200
    for i in range(len(row)):
        tbody += "<tr><td>%s</td>"%str(row[i])
        for j in range(len(aggr[0])):
            val = aggr[i][j]
            r = ceil(r_min-((val-min_val)*1.0/(max_val-min_val))*(r_min-r_max))
            g = ceil(g_min-((val-min_val)*1.0/(max_val-min_val))*(g_min-g_max))
            b = ceil(b_min-((val-min_val)*1.0/(max_val-min_val))*(b_min-b_max))
            if val==0:
                r = 255
                g = 255
                b = 255
            tbody += '<td style="background-color:rgb(%d,%d,%d);">%s</td>'%(r,g,b,str(val))
        tbody += "</tr>"
        cs = '<tr>Color Scale</tr><tr>'
        for i in range(0,11):
            r = r_min-(i/10.0)*(r_min-r_max)
            g = g_min-(i/10.0)*(g_min-g_max)
            b = b_min-(i/10.0)*(b_min-b_max)
            cs += '<td style="background-color:rgb(%d,%d,%d);color:rgb(%d,%d,%d);" class="cs-cell">hi</td>'%(r,g,b,r,g,b)
        cs += "</tr><tr><td>min</td>"+"<td></td>"*9+"<td>max</td></tr>"
    return tbody, cs
