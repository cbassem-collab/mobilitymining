import json
import csv
from os import listdir,mkdir
from os.path import join

def readAlltojson():
    dirs = listdir("Data")
    for person in dirs:
        print("Person: " + person)
        readThenDumpOne(person)

def readThenDumpOne(person):
    readPath = "Data/" + person + "/Trajectory"
    dumpPath = "Datastore/" + person
    mkdir(dumpPath)
    dirs = listdir(readPath)
    for oneDir in dirs:
        with open (join(dumpPath,oneDir.replace("plt","txt")),"w") as js:
            json.dump(readOneFile(join(readPath, oneDir)),js,indent=4)

def readOneFile(filename):
    with open (filename) as fl:
        locList = [readOneLine(line.strip()) for line in fl.readlines()[6:]]

    return locList

def readOneLine(line):
    info = line.split(",")
    locDict = {"latitude": info[0],
               "longtitude": info[1],
               "altitude": info[3],
               "date": info[5],
               "time": info[6]}
    return locDict

def readOneLine_CSV(line,person):
    info = line.split(",")
    locDict = {"user_id": person,
               "latitude": info[0],
               "longtitude": info[1],
               "timestamp": info[5] + " " + info[6]}
    return locDict

def readOneFile_CSV(filename,person):
    with open (filename) as fl:
        locList = [readOneLine_CSV(line.strip(),person) for line in fl.readlines()[6:]]

    return locList

def readOneToCSV(person):
    readPath = "Data/" + person + "/Trajectory"
    savePath = "Data_CSV/" + person
    mkdir(savePath)
    dirs = listdir(readPath)

    for oneDir in dirs:
      with open (join(savePath,oneDir.replace("plt","csv")),"w",newline="") as csv_file:
        fieldnames = ["user_id","latitude","longtitude","timestamp"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        loclist = readOneFile_CSV(join(readPath,oneDir),person)

        for locdict in loclist:
          writer.writerow(locdict)

def readAllToCSV():
    dirs = listdir("Data")
    for person in dirs:
        print("Person: " + person)
        readOneToCSV(person)

if __name__ == "__main__":
   readAllToCSV()