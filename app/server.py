from flask import Flask
import csv
from jinja2 import Template
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
    data=[]
    for row in csvreader:
        data.append(row)
    f.close()
    
    # Render data to html template
    template = Template(open('ptb.html').read())
    return template.render(
        data = data
    )


@app.route("/pivotTable")
def pivotTable():
    return "I'm a pivot table"


@app.route("/visualisation")
def visualisation():
    return

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
