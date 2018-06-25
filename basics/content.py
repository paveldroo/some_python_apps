from datetime import datetime

files = ['file1.txt', 'file2.txt', 'file3.txt']
timestamp = str(datetime.now())

def merging(files, timestamp):
    with open(timestamp, 'a+') as myfile:
        for file in files:
            with open(file, 'r') as s:
                myfile.write(s.read())

merging(files, timestamp)

