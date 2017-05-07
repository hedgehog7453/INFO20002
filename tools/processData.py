import csv

inputfile = open('Traffic_Violations.csv', 'rb')
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
2 Agency
3 SubAgency
4 Description
5 Location
6 Latitude
7 Longitude
8 Accident
9 Belts
10 Personal Injury
11 Property Damage
12 Fatal
13 Commercial License
14 HAZMAT
15 Commercial Vehicle
16 Alcohol
17 Work Zone
18 State
19 VehicleType
20 Year
21 Make
22 Model
23 Color
24 Violation Type
25 Charge
26 Article
27 Contributed To Accident
28 Race
29 Gender
30 Driver City
31 Driver State
32 DL State
33 Arrest Type
34 Geolocation
'''

# Read all data and save them into a list of lists
data = []
for row in csvreader:
    if (row[10]=="Yes" or row[12]=="Yes"):
        data.append(row)

print(len(data))


# Close the input file
inputfile.close()


myfile = open("output.csv", 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(attributes)
for rows in data:
    wr.writerow(rows)
