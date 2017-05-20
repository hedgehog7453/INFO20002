import csv

#inputfile = open('Traffic_Violations.csv', 'rb')
inputfile = open('dataset1.csv', 'rb')
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
0 0 0 Date Of Stop
1 1 1 Time Of Stop
    2 Agency
    3 SubAgency
2 2 4 Description
    5 Location
    6 Latitude
    7 Longitude
    8 Accident
3 3 9 Belts
4 4 10 Personal Injury
    11 Property Damage
5 5 12 Fatal
6 6 13 Commercial License
    14 HAZMAT
    15 Commercial Vehicle
7 7 16 Alcohol
  8 17 Work Zone
8 9 18 State
9 10 19 VehicleType
10 11 20 Year
11 12 21 Make
12 13 22 Model
13 14 23 Color
14 15 24 Violation Type
     25 Charge
     26 Article
     27 Contributed To Accident
  16 28 Race
  17 29 Gender
     30 Driver City
     31 Driver State
     32 DL State
     33 Arrest Type
     34 Geolocation
'''

# attr_new = []
# attr_new.append(row[0])
# attr_new.append(row[1])
# attr_new.append(row[2])
# attr_new.append(row[3])
# attr_new.append(row[4])
# attr_new.append(row[5])
# attr_new.append(row[6])
# attr_new.append(row[7])
# attr_new.append(row[9])
# attr_new.append(row[10])
# attr_new.append(row[11])
# attr_new.append(row[12])
# attr_new.append(row[13])
# attr_new.append(row[14])
# attr_new.append(row[15])

attr_new = []
attr_new.append(row[0])
attr_new.append(row[1])
attr_new.append(row[4])
attr_new.append(row[9])
attr_new.append(row[10])
attr_new.append(row[13])
attr_new.append(row[15])
attr_new.append(row[19])
attr_new.append(row[20])
attr_new.append(row[21])
attr_new.append(row[22])
attr_new.append(row[23])
attr_new.append(row[28])
attr_new.append(row[29])
attr_new.append(row[34])


# Read all data and save them into a list of lists
data = []
#states = {}
for row in csvreader:
    # if row[18] not in states.keys():
    #     states[row[18]] = 0
    # if row[18] in states.keys() and row[10] == "Yes":
    #     states[row[18]] += 1
    # if (row[18]=="NY"):
    #     data.append(row)
    data_row = []
    data_row.append(row[0])
    data_row.append(row[1])
    data_row.append(row[4])
    data_row.append(row[9])
    data_row.append(row[10])
    data_row.append(row[13])
    data_row.append(row[15])
    data_row.append(row[19])
    data_row.append(row[20])
    data_row.append(row[21])
    data_row.append(row[22])
    data_row.append(row[23])
    data_row.append(row[28])
    data_row.append(row[29])
    data_row.append(row[34])
    data.append(data_row)

print(len(data))
# print states


# Close the input file
inputfile.close()


myfile = open("output.csv", 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(attr_new)
for row in data:
    wr.writerow(row)
