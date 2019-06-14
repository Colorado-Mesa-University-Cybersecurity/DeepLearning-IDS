import sys
import operator
import os

folderPath = 'results/fastai'


def main(inputFile):
    results = []
    inputFile = os.path.join(folderPath, inputFile)
    outputFile = '{}.ordered'.format(inputFile)
    with open(inputFile, 'r') as fin:
        data = fin.readlines()

    for line in data:
        values = line.split()
        acc = values[1]
        std_dev = values[3]
        acc = acc.replace(':', '')
        std_dev = std_dev.replace(':', '')
        results.append([float(acc), float(std_dev)])

    # sort by secondary key, std. deviation in ascending order
    results.sort(key=operator.itemgetter(1))
    # sort by accuracy in descending order
    results.sort(key=operator.itemgetter(0), reverse=True)
    # print(results)
    with open(outputFile, 'w') as fout:
        for acc, std in results:
            fout.write("accuracy: {:.2f}% std_dev: {:.2f}\n".format(
                acc, std))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python topaccuracy.py inputFile')
        print('Average result will be in inputFile.avg file')
        sys.exit()

    main(sys.argv[1])
    print('all done!')
