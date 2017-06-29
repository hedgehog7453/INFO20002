# Traffic Violations in New York

This is a group project of subject INFO20002 Foundations of Informatics at the University of Melbourne. 

Group members: Jiayu Li, Yifan Wang, Chaoxin Wu


## To Run the Application

To run this web app, please follow the instruction:
1. Under the 'app' folder, run 'python server.py' in any command-line tool
2. When server is setup, in a web browser (google chrome is prefered), go to the address 'http://localhost:5000/'


## Application Structure

### Raw Data

A bootstrap table that displays the raw dataset used for the project. It provides sorting, searching and pagination. 


### Pivot Table Builder

This page allows user to observe the data by building a pivot table. User needs to input row, column, aggregation attribute, aggregation method, and an optional filter (the attribute to filter on, filter condition, and filter value). It directs to the pivot table page after clicking "Create Pivot Table" button. 


### Hypothesis and Observation

This page introduces 5 hypotheses based on the dataset and our observations after visualising the data.


## Dataset

### Data Source

Dataset source: DataMontgomery website
https://data.montgomerycountymd.gov/Public-Safety/Traffic-Violations/4mse-ku6q

Contains data from all states in the U.S. from 2012 till March 2017. 

Original data set size:
Rows: 1048576 Columns: 35


### Data Processing

Some data in the dataset is removed for project purpose.
1. We deleted all states except for NY
2. We deleted the attributes that we're not interested in (e.g. agency, subagency)
3. We deleted rows with invalid data (e.g. year '9999' and state '??')
4. We added new columns that are helpful for data analysis (e.g. year, month, time period when traffic violations happen)
 
Eventually our new dataset has 17 columns and 3568 rows.


## Additional Notes

Spreadsheet used to generate data for data visualisation:
`/dataset_excel.xlsx`

Presentation slides:
`/Presentation slides.pptx`
