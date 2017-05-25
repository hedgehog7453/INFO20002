from flask import Flask, request
import csv
from jinja2 import Template
from ptb import *
import numpy 
import pandas
# import sys

# reload(sys)
# sys.setdefaultencoding('utf8')

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route("/")
def root():
    return app.send_static_file('index.html')


@app.route("/rawData")
def rawData():
    # Read data
    data = readcsv()

    # Render data to html template
    template = Template(open('rawData.html').read())
    return template.render(
        data = data,
        datalen = len(data)
    )


@app.route("/pivotTableBuilder")
def pivotTableBuilder():
    # Read attributes
    data = readcsv()
    attr = data[0]
    attr_trimmed = []
    for a in attr:
        attr_trimmed.append(a.replace(" ", "").lower())
    # Render data to html template
    template = Template(open('ptb.html').read())
    return template.render(
        attr = attr, 
        attr_trimmed = attr_trimmed, 
        attr_len = len(attr)
    )


@app.route("/pivotTable", methods=['GET', 'POST'])
def pivotTable():
    row = request.form['row']
    col = request.form['col']
    aggr_m = request.form['aggregation_method']
    aggr_a = request.form['aggregation_attr']
    filter_a = request.form['filter_attr']
    filter_cond = request.form['filter_cond']
    filter_val = request.form['filter_val']

    # trimmed attribute to original attribute
    t2o = {
        "dateofstop": "Date Of Stop", 
        "monthofstop": "Month Of Stop",
        "yearofstop": "Year Of Stop",
        "timeofstop": "Time Of Stop", 
        "timeperiod": "Time Period",
        "description": "Description", 
        "belts": "Belts", 
        "personalinjury": "Personal Injury", 
        "commerciallicense": "Commercial License", 
        "commercialvehicle": "Commercial Vehicle", 
        "vehicletype": "Vehicle Type", 
        "year": "Year", 
        "make": "Make", 
        "model": "Model", 
        "color": "Color", 
        "race": "Race", 
        "gender": "Gender"
    }

    agg_d = {
        "count": "Count of",
        "max": "Maximum of",
        "min": "Minimum of"
    }

    if filter_val=="":
        ptb_str = 'Row: ' + t2o[str(row)] + '; ' + 'Column: ' + t2o[str(col)] + '<br>' + 'Aggregation method: ' + str(aggr_m) + '; ' + 'Aggregation attribute: ' + t2o[str(aggr_a)] + '<br>' + 'Filter attribute: ' + t2o[str(filter_a)] + '; ' + 'Filter method: ' + str(filter_cond) + '; ' + 'Filter value: none<br>'
    else:
        ptb_str = 'Row: ' + t2o[str(row)] + '; ' + 'Column: ' + t2o[str(col)] + '<br>' + 'Aggregation method: ' + str(aggr_m) + '; ' + 'Aggregation attribute: ' + t2o[str(aggr_a)] + '<br>' + 'Filter attribute: ' + t2o[str(filter_a)] + '; ' + 'Filter method: ' + str(filter_cond) + '; ' + 'Filter value: ' + str(filter_val) + '<br>'
    
    pt = pivot_table_builder_func(t2o[str(row)], t2o[str(col)], aggr_m, t2o[str(aggr_a)])
    row_val = pt.index.values
    col_val = pt.columns.values
    aggr_a_val = pt[t2o[str(aggr_a)]].values    

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

    template = Template(open('pivotTable.html').read())
    return template.render(
        ptb_str = ptb_str,
        row = t2o[str(row)],
        column = t2o[str(col)],
        val = agg_d[str(aggr_m)]+" "+t2o[str(aggr_a)],
        row_val = row_val,
        row_val_len = len(row_val),
        col_val = col_val,
        col_val_len = len(col_val),
        aggr_a_val = aggr_a_val_int,
        r = len(aggr_a_val_int),
        c = len(aggr_a_val_int[0]),
        col_span = str(len(col_val)),
        col_span_val = str(len(col_val)+1)
    )


@app.route("/visualisation")
def visualisation():
    template = Template(open('observation.html').read())
    return template.render()

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
