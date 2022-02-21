import csv
import numpy as np 
def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    
    return{"x":marks_in_percentage,"y":days_present}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between marks ans days is:\n-->",correlation[0,1])

def setup():
    data_path = "./data/data.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()