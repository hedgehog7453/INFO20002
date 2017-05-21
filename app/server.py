from flask import Flask, request
import csv
from jinja2 import Template
from ptb import *
app = Flask(__name__, static_folder='.', static_url_path='')


@app.route("/")
def root():
    return app.send_static_file('index.html')


@app.route("/rawData")
def rawData():
    # Read data
    f = open("assets/dataset.csv")
    csvreader = csv.reader(f, delimiter=',', skipinitialspace=True)
    data = []
    for row in csvreader:
        data.append(row)
    f.close()

    # Render data to html template
    template = Template(open('rawData.html').read())
    return template.render(
        data = data,
        datalen = len(data)
    )


@app.route("/pivotTableBuilder")
def pivotTableBuilder():
    #Read cols
    f = open("assets/dataset.csv")
    csvreader = csv.reader(f, delimiter=',', skipinitialspace=True)
    attr = []
    attr_trimmed = []
    for row in csvreader:
        attr = row
        break
    f.close()
    
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
        "timeofstop": "Time Of Stop", 
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
        "gender": "Gender", 
        "geolocation": "Geolocation"
    }

    if filter_val=="":
        ptb_str = 'Row: ' + t2o[str(row)] + '; ' + 'Column: ' + t2o[str(col)] + '<br>' + 'Aggregation method: ' + str(aggr_m) + '; ' + 'Aggregation attribute: ' + t2o[str(aggr_a)] + '<br>' + 'Filter attribute: ' + t2o[str(filter_a)] + '; ' + 'Filter method: ' + str(filter_cond) + '; ' + 'Filter value: None<br>'
    else:
        ptb_str = 'Row: ' + t2o[str(row)] + '; ' + 'Column: ' + t2o[str(col)] + '<br>' + 'Aggregation method: ' + str(aggr_m) + '; ' + 'Aggregation attribute: ' + t2o[str(aggr_a)] + '<br>' + 'Filter attribute: ' + t2o[str(filter_a)] + '; ' + 'Filter method: ' + str(filter_cond) + '; ' + 'Filter value: ' + str(filter_val) + '<br>'
    
    #

    template = Template(open('pivotTable.html').read())
    return template.render(
        ptb_str = ptb_str
    )


@app.route("/visualisation")
def visualisation():
    return

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
