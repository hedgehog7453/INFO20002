from flask import Flask, request
import csv
from jinja2 import Template
from ptb import *
import numpy 
import pandas

app = Flask(__name__, static_folder='.', static_url_path='')


# Landing page
@app.route("/")
def root():
    return app.send_static_file('index.html')


# Raw data page
@app.route("/rawData")
def rawData():
    # Read data
    data = readcsv()
    # Render data to html template
    template = Template(open('rawData.html').read())
    return template.render(
        attr_o = ORIGINAL_COL,
        attrlen = len(ORIGINAL_COL),
        data = data,
        datalen = len(data)
    )


# Pivot table builder page
@app.route("/pivotTableBuilder")
def pivotTableBuilder():
    # Render data to html template
    template = Template(open('ptb.html').read())
    return template.render(
        attr = TRIMMED_COL, 
        attr_o = ORIGINAL_COL, 
        attr_len = len(ORIGINAL_COL)
    )


# Pivot table page
@app.route("/pivotTable", methods=['GET', 'POST'])
def pivotTable():
    # Acquire the data from pivot table builder page
    try:
        row = request.form['row']
        col = request.form['col']
        aggr_m = request.form['aggregation_method']
        aggr_a = request.form['aggregation_attr']
        filter_a = request.form['filter_attr']
        filter_cond = request.form['filter_cond']
        filter_val = request.form['filter_val']
    except:
        return "Bad request. <br>Please click <a href='/pivotTableBuilder'>here</a> to build pivot table."

    # aggregation method dictionary (for displaing on the webpage)
    agg_d = {
        "count": "Count of",
        "max": "Maximum of",
        "min": "Minimum of"
    }

    # String the indicates the requirement from the selection in pivot table builder
    if filter_val=="":
        ptb_str = 'Row: ' + t2o2t(str(row)) + '; ' + 'Column: ' + t2o2t(str(col)) + '<br>' + 'Aggregation method: ' + str(aggr_m) + '; ' + 'Aggregation attribute: ' + t2o2t(str(aggr_a)) + '<br>' + 'Filter attribute: ' + t2o2t(str(filter_a)) + '; ' + 'Filter method: ' + str(filter_cond) + '; ' + 'Filter value: none<br>'
    else:
        ptb_str = 'Row: ' + t2o2t(str(row)) + '; ' + 'Column: ' + t2o2t(str(col)) + '<br>' + 'Aggregation method: ' + str(aggr_m) + '; ' + 'Aggregation attribute: ' + t2o2t(str(aggr_a)) + '<br>' + 'Filter attribute: ' + t2o2t(str(filter_a)) + '; ' + 'Filter method: ' + str(filter_cond) + '; ' + 'Filter value: ' + str(filter_val) + '<br>'
    
    # Build the pivot table
    pt = pivot_table_builder_func(str(row), str(col), aggr_m, str(aggr_a), filter_a, filter_cond, filter_val)
    row_val = pt.index.values
    col_val = pt.columns.values
    aggr_a_val = pt[str(aggr_a)].values    

    # Transfer all numbers to integer, and 'nan' to 0
    aggr_a_val_int = []
    aggr_a_val_int_row = []
    for i in aggr_a_val:
        for j in i:
            try:
                aggr_a_val_int_row.append(int(j))
            except ValueError:
                aggr_a_val_int_row.append(0)
        aggr_a_val_int.append(aggr_a_val_int_row)
        aggr_a_val_int_row = []

    color_scale = add_style(row_val, aggr_a_val_int)
    tbody = color_scale[0]
    cs = color_scale[1]

    # Render data to html template
    template = Template(open('pivotTable.html').read())
    return template.render(
        ptb_str = ptb_str,
        row = t2o2t(str(row)),
        column = t2o2t(str(col)),
        val = agg_d[str(aggr_m)]+" "+t2o2t(str(aggr_a)),
        col_val = col_val,
        col_val_len = len(col_val),
        col_span = str(len(col_val)),
        col_span_val = str(len(col_val)+1),
        tbody = tbody,
        color_scale = cs
    )


# Observation page
@app.route("/visualisation")
def visualisation():
    # Render html template
    template = Template(open('observation.html').read())
    return template.render()


# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
