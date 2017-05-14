from flask import Flask
import csv
app = Flask(__name__, static_folder='.', static_url_path='')

def htmlTemplate(body):
    return """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Project Phase 3</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="style.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    </head>
    <body>
        <div class="loader"></div>
        <table class="table table-bordered table-condensed">
            <thead>
                <tr>
    """ + body + """
    </body>
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

    htmlBody = ""
    
    for attr in data[0]:
        htmlBody += "<th>"+attr+"</th>"
    htmlBody += "</tr>"

    for i in range(1,len(data)):
        htmlBody += "<tr>"
        for cell in data[i]:
            htmlBody += "<td>"+cell+"</td>"
        htmlBody += '</tr>'

    return htmlTemplate(htmlBody)

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