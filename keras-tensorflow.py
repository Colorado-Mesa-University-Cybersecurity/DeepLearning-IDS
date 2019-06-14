import csv
import os
import sys
import numpy as np
import pandas as pd
import operator

from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.preprocessing import LabelEncoder
from keras.utils.np_utils import to_categorical
from sklearn.utils import shuffle
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasClassifier

assert K.backend() == 'tensorflow', 'set backend to tensorflow in ~/.keras/keras.json file'

dataPath = 'CleanedTrafficData'  # use your path
resultPath = 'results/tensorflow'
if not os.path.exists(resultPath):
    print('result path {} created.'.format(resultPath))
    os.mkdir(resultPath)

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


def multilass_baseline_model():
    # https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/
    model = Sequential()
    model.add(Dense(79, activation='relu', input_dim=79))
    model.add(Dense(79, activation='relu'))
    model.add(Dense(3, activation='softmax')) # softmax recommended for multi-class classification problem
    # compile model - for multi-class classifier

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def binary_baseline_model():
    # https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/
    model = Sequential()
    model.add(Dense(79, activation='relu', input_dim=79))
    model.add(Dense(79, activation='relu', input_dim=79))
    model.add(Dense(79, activation='relu', input_dim=79))

    #model.add(Dense(79, activation='relu'))
    # sigmoid
    model.add(Dense(2, activation='softmax'))
    # compile model - for multi-class classifier

    model.compile(optimizer='adam',
                  loss='binary_crossentropy', metrics=['accuracy'])
    return model


def experiment(dataFile, optimizer, epochs=10, batch_size=100):
    seed = 7
    np.random.seed(seed)
    cvscores = []
    print('optimizer: {} epochs: {} batch_size: {}'.format(
        optimizer, epochs, batch_size))
    data = loadData(dataFile)
    data_y = data.pop('Label')
    # transform named labels into numberical values
    encoder = LabelEncoder()
    encoder.fit(data_y)
    data_y = encoder.transform(data_y)
    dummy_y = to_categorical(data_y)
    data_x = data.values
    # define 5-fold cross validation test harness
    kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
    inputDim = len(data_x[0])
    print('inputdim =', inputDim)
    estimater = KerasClassifier(
        build_fn=binary_baseline_model, epochs=epochs, batch_size=batch_size, verbose=1)
    results = cross_val_score(estimater, data_x, dummy_y, cv=kfold)
    # create model\
    # build a simple, fully-connected network (multi-layer perceptron)

    # train the model, iterating on the data in batches of batch_size
    # model.fit(data_x[train], data_y[train], epochs=epochs,
    #          batch_size = batch_size, verbose = 0)
    # evaluate the model
    # scores = model.evaluate(data_x[test], data_y[test], verbose=0)
    acc, std_dev = results.mean()*100, results.std()*100
    print('Baseline: accuracy: {:.2f}%: std-dev: {:.2f}%'.format(acc, std_dev))
    # cvscores.append(scores[1]*100)
    resultFile = os.path.join(resultPath, dataFile)
    with open('{}.result'.format(resultFile), 'a') as fout:
        fout.write('accuracy: {:.2f} std-dev: {:.2f}\n'.format(acc, std_dev))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python kerasframeworks.py inputFile.csv optimizer')
        print('optimizers: adam, rmsprop, sgd, adagrad, ')
        sys.exit()

    # getData()
    experiment(sys.argv[1], sys.argv[2])
