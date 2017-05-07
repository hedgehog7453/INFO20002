from flask import Flask
import csv
app = Flask(__name__, static_folder='.', static_url_path='')

import time

@app.route("/")
def root():
    f = open("index.html")
    s = f.read()
    f.close()
    return s

@app.route("/rawData")
def rawData():
    f = open("dataset.csv")
    data = f.readline()
    f.close()
    return data

@app.route("/pivotTableBuilder")
def pivotTableBuilder():
    # TODO: Alan
    return "??"

@app.route("/pivotTable")
def pivotTable():
    return

@app.route("/visualisation")
def visualisation():
    return


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000) # use port=80 on windows