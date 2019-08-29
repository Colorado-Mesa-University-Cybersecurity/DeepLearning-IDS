import csv
import sys
import datetime
from dateutil import parser
from collections import defaultdict
import os


def cleanData(inFile, outFile):
    count = 1
    stats = {}
    dropStats = defaultdict(int)
    print('cleaning {}'.format(inFile))
    with open(inFile, 'r') as csvfile:
        data = csvfile.readlines()
        totalRows = len(data)
        print('total rows read = {}'.format(totalRows))
        header = data[0]
        for line in data[1:]:
            line = line.strip()
            cols = line.split(',')
            key = cols[-1]
            if line.startswith('D') or line.find('Infinity') >= 0 or line.find('infinity') >= 0:
                dropStats[key] += 1
                continue

            dt = parser.parse(cols[2])  # '1/3/18 8:17'
            epochs = (dt - datetime.datetime(1970, 1, 1)).total_seconds()
            cols[2] = str(epochs)
            line = ','.join(cols)
            # clean_data.append(line)
            count += 1

            if key in stats:
                stats[key].append(line)
            else:
                stats[key] = [line]

            """
            if count >= 1000:
                break
            """

    with open(outFile+".csv", 'w') as csvoutfile:
        csvoutfile.write(header)
        with open(outFile + ".stats", 'w') as fout:
            fout.write('Total Clean Rows = {}; Dropped Rows = {}\n'.format(
                count, totalRows - count))
            for key in stats:
                fout.write('{} = {}\n'.format(key, len(stats[key])))
                line = '\n'.join(stats[key])
                csvoutfile.write('{}\n'.format(line))
                with open('{}-{}.csv'.format(outFile, key), 'w') as labelOut:
                    labelOut.write(header)
                    labelOut.write(line)
            for key in dropStats:
                fout.write('Dropped {} = {}\n'.format(key, dropStats[key]))

    print('all done writing {} rows; dropped {} rows'.format(
        count, totalRows - count))


def cleanAllData():
    # inputDataPath = os.path.join(
    #    os.path.dirname(os.path.realpath(__file__)), )
    inputDataPath = '../ProcessedTrafficData'
    outputDataPath = '../NewCleanedData'
    if (not os.path.exists(outputDataPath)):
        os.mkdir(outputDataPath)

    files = os.listdir(inputDataPath)
    for file in files:
        if file.startswith('.'):
            continue
        if os.path.isdir(file):
            continue
        outFile = os.path.join(outputDataPath, file)
        inputFile = os.path.join(inputDataPath, file)
        cleanData(inputFile, outFile)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python data_cleanup.py inputFile.csv outputFile')
    elif sys.argv[1] == 'all':
        cleanAllData()
    else:
        cleanData(sys.argv[1], sys.argv[2])
