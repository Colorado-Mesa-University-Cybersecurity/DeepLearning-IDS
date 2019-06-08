import csv
import sys
import datetime
from dateutil import parser


def cleanData(inFile, outFile):
    count = 1
    stats = {}
    with open(inFile, 'r') as csvfile:
        data = csvfile.readlines()
        totalRows = len(data)
        print('total rows read = {}'.format(totalRows))
        header = data[0]
        for line in data[1:]:
            line = line.strip()
            if line.startswith('D') or line.find('Infinity') >= 0 or line.find('infinity') >= 0:
                continue
            cols = line.split(',')

            dt = parser.parse(cols[2])  # '1/3/18 8:17'
            epochs = (dt - datetime.datetime(1970, 1, 1)).total_seconds()
            cols[2] = str(epochs)
            line = ','.join(cols)
            # clean_data.append(line)
            count += 1
            key = cols[-1]
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

    print('all done writing {} rows; dropped {} rows'.format(
        count, totalRows - count))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python data_cleanup.py inputFile.csv outputFile')
    else:
        cleanData(sys.argv[1], sys.argv[2])
