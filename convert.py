import json
from collections import deque
import os
import csv

class jsonToExcel:
    def __init__(self):
        pass

    def main(self):
        self.getResultsFromData()
    
    def retrieveJsonFiles(self):
        json_data = list()
        with open ("myfile.json", "r") as f:
            json_data.append(json.load(f))
        return json_data
    
    def findlist(self):
        json_data = self.retrieveJsonFiles()
        final_json = list()
        uid = [[y for y in x.keys()] for x in json_data][0]
        jp = json_data[0]
        for key, value in jp.items():
            for x in uid:
                if x == key:
                    final_v = list(value.values())
                    dfinal_v = deque(final_v)
                    dfinal_v.appendleft(x)
                    ffinal_v = list(dfinal_v)
                    final_json.append(ffinal_v)
        return final_json

    def getResultsFromData(self):
        headers = ['Uid','Firstname','Lastname', 'No of Attendance', 'Last Attendance', 'Next Attendance']
        with open ('data_file.csv', 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(headers)
            csv_writer.writerows(self.findlist())

def main():
    jToExc = jsonToExcel()
    jToExc.main()
   

if __name__ == "__main__":
    main()