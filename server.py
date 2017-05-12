from flask import Flask
import csv
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

    html = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Project Phase 3</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="style.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script type="text/javascript">
            $(window).load(function() {
                $(".loader").fadeOut("slow");
            });
        </script>
    </head>
    <body>
        <div class="loader"></div>
        <table class="table table-bordered table-condensed">
            <thead>
                <tr>
    """
    
    for attr in data[0]:
        html += "<th>"+attr+"</th>"
    html += "</tr>"

    for i in range(1,len(data)):
        html += "<tr>"
        for cell in data[i]:
            html += "<td>"+cell+"</td>"
        html += '</tr>'

    html += """
    </body>
    
</html>
    """
    return html

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