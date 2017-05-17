from flask import Flask
import csv
app = Flask(__name__, static_folder='.', static_url_path='')

def htmlTemplate(title, body, header=""):
    return """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>""" + title + """</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="style.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
        """ + header + """
    </head>
    """ + body + """
</html>
    """

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
    # Generate HTML body
    htmlBody = """<div class="loader"></div>
    <table class="table table-bordered table-condensed">
    <tr>"""
    for attr in data[0]:
        htmlBody += "<th>"+attr+"</th>"
    htmlBody += "</tr>"
    for i in range(1,len(data)):
        htmlBody += "<tr>"
        for cell in data[i]:
            htmlBody += "<td>"+cell+"</td>"
        htmlBody += '</tr>'
    # Loader
    header = """<script type="text/javascript">
                    $(window).load(function() {
                        $(".loader").fadeOut("slow");
                    });
                </script>"""
    return htmlTemplate("Raw Data", htmlBody, header)

@app.route("/pivotTableBuilder")
def pivotTableBuilder():
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
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
        </select>
        <input class="form-control">
    </div>
    <div class="form-group col-md-6 selector">
        <label for="sel1">Row Label</label>
        <select class="form-control">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
        </select>
    </div>
    <div class="form-group col-md-6 selector">
        <label for="sel1">Column Label</label>
        <select class="form-control">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
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
        <select class="form-control">
            <option>1</option>
            <option>2</option>
        </select>
    </div>
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