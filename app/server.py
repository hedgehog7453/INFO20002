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
    
    body = """<body id="bg-img2">
    <h2>Pivot Table Builder</h2>
    <div class="form-group col-md-6 selector">
        <label for="sel1">Report Filter</label>
        <select class="form-control">"""
        
    for attr in data[0]:
        body += "<option>"+attr+"</option>"
        
    body +="""
        </select>
        <select class="form-control">
            <option>is anything</option>
            <option>=</option>
            <option>></option>
            <option>>=</option>
            <option><</option>
            <option><=</option>
            <option>!=</option>
            <option>contains</option>
            <option>doesn't contain</option>
            <option>is Yes</option>
            <option>is No</option>
        </select>
        <input class="form-control">
    </div>  
    <div class="form-group col-md-6 selector">
        <label for="sel1">Row Label</label>
        <select class="form-control">
        <option>is No</option>
        </select>
    </div>
    <div class="form-group col-md-6 selector">
        <label for="sel1">Column Label</label>
        <select class="form-control">"""
    for attr in data[0]:
        body += "<option>"+attr+"</option>"
        
    body +="""
        </select>
    </div>
    <div class="form-group col-md-6 selector">
        <label for="sel1">Aggregation</label>
        <select class="form-control">
            <option>count of</option>
            <option>sum of</option>
            <option>average of</option>
            <option>maximum of</option>
            <option>minimun of</option>
        </select>
        <select class="form-control">"""
    for attr in data[0]:
        body += "<option>"+attr+"</option>"
    body +="""
        </select>
    </div>
     <form>
        <input type="button" class="btn btn-primary" onclick="location.href='/pivotTable';" value="Pivot Table" />
    </form>>
</body>"""
    
    return htmlTemplate("Pivot Table Builder", body)

@app.route("/pivotTable")
def pivotTable():
    return

@app.route("/visualisation")
def visualisation():
    return

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
