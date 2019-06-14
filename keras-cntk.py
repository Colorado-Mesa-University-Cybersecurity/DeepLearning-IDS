
# Keras-cntk backend is not running, as I've not figure out how to install cntk!

import os
from sklearn.model_selection import StratifiedKFold
import operator
import pandas as pd
import numpy
import sys
import csv

# import keras as ks
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense, Activation

assert K.backend() == 'cntk', 'set backend to cntk in ~/.keras/keras.json file'


dep_var = 'Label'
cat_names = ['Dst Port', 'Protocol']
cont_names = ['Timestamp', 'Flow Duration', 'Tot Fwd Pkts',
              'Tot Bwd Pkts', 'TotLen Fwd Pkts', 'TotLen Bwd Pkts', 'Fwd Pkt Len Max',
              'Fwd Pkt Len Min', 'Fwd Pkt Len Mean', 'Fwd Pkt Len Std',
              'Bwd Pkt Len Max', 'Bwd Pkt Len Min', 'Bwd Pkt Len Mean',
              'Bwd Pkt Len Std', 'Flow Byts/s', 'Flow Pkts/s', 'Flow IAT Mean',
              'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Tot',
              'Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max', 'Fwd IAT Min',
              'Bwd IAT Tot', 'Bwd IAT Mean', 'Bwd IAT Std', 'Bwd IAT Max',
              'Bwd IAT Min', 'Fwd PSH Flags', 'Bwd PSH Flags', 'Fwd URG Flags',
              'Bwd URG Flags', 'Fwd Header Len', 'Bwd Header Len', 'Fwd Pkts/s',
              'Bwd Pkts/s', 'Pkt Len Min', 'Pkt Len Max', 'Pkt Len Mean',
              'Pkt Len Std', 'Pkt Len Var', 'FIN Flag Cnt', 'SYN Flag Cnt',
              'RST Flag Cnt', 'PSH Flag Cnt', 'ACK Flag Cnt', 'URG Flag Cnt',
              'CWE Flag Count', 'ECE Flag Cnt', 'Down/Up Ratio', 'Pkt Size Avg',
              'Fwd Seg Size Avg', 'Bwd Seg Size Avg', 'Fwd Byts/b Avg',
              'Fwd Pkts/b Avg', 'Fwd Blk Rate Avg', 'Bwd Byts/b Avg',
              'Bwd Pkts/b Avg', 'Bwd Blk Rate Avg', 'Subflow Fwd Pkts',
              'Subflow Fwd Byts', 'Subflow Bwd Pkts', 'Subflow Bwd Byts',
              'Init Fwd Win Byts', 'Init Bwd Win Byts', 'Fwd Act Data Pkts',
              'Fwd Seg Size Min', 'Active Mean', 'Active Std', 'Active Max',
              'Active Min', 'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min']

dataPath = 'CleanedTrafficData'  # use your path
resultPath = 'results/cntk'
if not os.path.exists(resultPath):
    print('result path {} created.'.format(resultPath))
    os.mkdir(resultPath)


def loadData(fileName):
    dataFile = os.path.join(dataPath, fileName)
    pickleDump = '{}.pickle'.format(dataFile)
    if os.path.exists(pickleDump):
        df = pd.read_pickle(pickleDump)
    else:
        df = pd.read_csv(dataFile)
        df = df.dropna()
        df = shuffle(df)
        df.to_pickle(pickleDump)
    return df


# k-fold cross validation:
# https://machinelearningmastery.com/evaluate-performance-deep-learning-models-keras/

def experiment(dataFile, optimizer, epochs, batch_size):
    seed = 7
    numpy.random.seed(seed)
    cvscores = []
    print('optimizer: {} epochs: {} batch_size: {}'.format(
        optimizer, epochs, batch_size))
    data = loadData(dataFile)
    data_y = data.pop('Label').values
    data_x = data.as_matrix()
    # define 5-fold cross validation test harness
    kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    for train, test in kfold.split(data_x, data_y):
        # create model\
        # build a simple, fully-connected network (multi-layer perceptron)
        model = Sequential()
        model.add(Dense(80, activation='relu', input_dim=80))
        model.add(Dense(80, activation='relu', input_dim=80))
        model.add(Dense(1, activation='softmax'))  # sigmoid
        # compile model - for binary classifier
        model.compile(optimizer=optimizer,
                      loss='binary_crossentropy', metrics=['accuracy'])
        # train the model, iterating on the data in batches of batch_size
        model.fit(data_x[train], data_y[train], epochs=10,
                  batch_size=100, verbose=0)
        # evaluate the model
        scores = model.evaluate(data_x[test], data_y[test], verbose=0)
        print('{}: {:.2f}%'.format(model.metrics_names[1], scores[1]*100))
        cvscores.append(scores[1]*100)
        resultFile = os.path.join(resultPath, dataFile)
        with open('{}.result'.format(resultFile), 'a') as fout:
            fout.write(
                'accuracy: {:.2f} std-dev: {:.2f}\n'.format(np.mean(cvscores), np.std(cvscores)))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python kerasframeworks.py inputFile.csv optimizer')
        print('optimizers: adam, rmsprop, sgd, adagrad, ')
        sys.exit()

    # getData()
    experiment(sys.argv[1])
