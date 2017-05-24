import csv

inputfile = open('dataset.csv', 'rb')
csvreader = csv.reader(inputfile, delimiter=',', skipinitialspace=True)

# Save all attribute names in a list
for row in csvreader:
    l = len(row)
    attributes = row
    break

'''
0 Date Of Stop
1 Month Of Stop
2 Year Of Stop
3 Time Of Stop
4 Description
5 Belts
6 Personal Injury
7 Commercial License
8 Commercial Vehicle
9 VehicleType
10 Year
11 Make
12 Model
13 Color
14 Race
15 Gender
'''

# data = []
# newrow = []

# for row in csvreader:
#     # row.insert(1, row[0][:2])
#     # for i in range(len(row)):
#     #     if i!=1:
#     #         newrow.append(row[i])
#     # data.append(newrow)
#     # newrow = []
#     for cell in row:
#         if row.index(cell)==3:
#         #     if cell[1] == ':':
#         #         newcell = "0"+cell
#         #     else:
#         #         newcell = cell
#         #     newrow.append(newcell)
#         # else:
#         #     newrow.append(cell)
#         #     time = int(cell[:2])
#         #     if time<9:
#         #         next_time = "0"+str(time+1)
#         #     else:
#         #         next_time = str(time+1)
#         #     time_p = cell[:2]+"-"+next_time
#         #     newrow.append(cell)
#         #     newrow.append(time_p)
#         # else:
#         #     newrow.append(cell)

#     data.append(newrow)
#     newrow = []

s = ""
for row in csvreader:
    for cell in row:
        if row.index(cell)==4:
            s += " "+cell

print s
# Close the input file
#inputfile.close()


# myfile = open("output.csv", 'wb')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# wr.writerow(attributes)
# for row in data:
#     wr.writerow(row)

myfile = open("str.txt", "wb")
myfile.write(s)
myfile.close()