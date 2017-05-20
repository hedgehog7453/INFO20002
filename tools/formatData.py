import csv

inputfile = open('dataset.csv', 'rb')
csvreader = csv.reader(inputfile, delimiter=',', skipinitialspace=True)

# Save all attribute names in a list
for row in csvreader:
    l = len(row)
    attributes = row
    break

# i=0
# for entry in row:
#     print(str(i)+" "+entry)
#     i += 1

'''
0 Date Of Stop
1 Time Of Stop
2 Description
3 Belts
4 Personal Injury
5 Commercial License
6 Commercial Vehicle
7 VehicleType
8 Year
9 Make
10 Model
11 Color
12 Race
13 Gender
14 Geolocation
'''


# Read all data and save them into a list of lists
data = []
for row in csvreader:
    new_row = []
    for cell in row: 
        if row.index(cell) == 0:
            if (cell[1]) == "/":
                new_cell = "0"+cell
            else:
                new_cell = cell
            new_row.append(new_cell)
        else:
            new_row.append(cell)
    data.append(new_row)


# Close the input file
inputfile.close()


myfile = open("output.csv", 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(attributes)
for row in data:
    wr.writerow(row)
