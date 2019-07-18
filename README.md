# Deep Learning - IDS

Towards Developing a Network Intrusion Detection System using Deep Learning Techniques

## Introduction

In this project, we aim to explore the capabilities of various deep-learning frameworks in detecting
and classifying network intursion traffic with an eye towards designing a ML-based intrusion detection system.

## Dataset

-   Downloaded from: https://www.unb.ca/cic/datasets/ids-2018.html
-   contains: 7 csv preprocessed and labelled files, top feature selected files, orginal traffic data in pcap format and logs
-   used csv preprocessed and labelled files for this research project

## Data Cleanup

-   dropped rows with Infinitiy values
-   some files had repeated headers; dropped those
-   converted timestamp value that was date time format: 15-2-2018 to UNIX epoch since 1/1/1970
-   separated data based on attack types for each data file
-   ~20K rows were removed as a part of data cleanup
-   see data_cleanup.py script for this phase

## Dataset Summary

| File Name      | Traffic Type     | # Samples |
| -------------- | ---------------- | --------: |
| 02-14-2018.csv | Benign           |   663,808 |
|                | FTP-BruteForce   |   193,354 |
|                | SSH-Bruteforce   |   187,589 |
| 02-15-2018.csv | Benign           |   988,050 |
|                | DOS-GoldenEye    |    41,508 |
|                | DOS-Slowloris    |    10,990 |
| 02-16-2018.csv | Benign           |   446,772 |
|                | Dos-SlowHTTPTest |   139,890 |
|                | DoS-Hulk         |   461,912 |
| 02-22-2018.csv | Benign           | 1,042,603 |
|                | BruteForce-Web   |       249 |
|                | BruteForce-XSS   |        79 |
|                | SQL-Injection    |        34 |
| 02-23-2018.csv | Benign           | 1,042,301 |
|                | BruteForce-Web   |       362 |
|                | BruteForce-XSS   |       151 |
|                | SQL-Injection    |        53 |
| 03-01-2018.csv | Benign           |   235,778 |
|                | Infiltration     |    92,403 |
| 03-02-2018.csv | Benign           |   758,334 |
|                | BotAttack        |   286,191 |

| Traffic Type     | # Samples |
| ---------------- | --------: |
| Benign           | 5,177,646 |
| FTP-BruteForce   |   193,354 |
| SSH-BruteForce   |   187,589 |
| DOS-GoldenEye    |    41,508 |
| Dos-Slowloris    |    10,990 |
| Dos-SlowHTTPTest |   139,890 |
| Dos-Hulk         |   461,912 |
| BruteForce-Web   |       611 |
| BruteForce-XSS   |       230 |
| SQL-Injection    |        87 |
| Infiltration     |    92,403 |
| BotAttack        |   286,191 |
| Total Attack     | 1,414,765 |

## Deep Learning Frameworks

-   perfomance results using various deep learning frameworks are compared
-   10-fold cross-validation techniques was used to validate the model

### FastAI

-   https://www.fast.ai/
-   uses PyTorch, https://pytorch.org/ as the backend

### Keras

-   https://keras.io/
-   using TensorFlow and Theano as backend
-   https://www.TensorFlow.org/
-   https://github.com/Theano/Theano

## Experiment Results

### Using CPU

| Dataset     | Framework         | Accuracy (%) | Std-Dev | CPU Time (~mins) |
| ----------- | ----------------- | -----------: | ------: | ---------------: |
| 02-14-2018  | FastAI            |        99.85 |    0.07 |               \* |
|             | Keras-TensorFlow  |        98.80 |      \* |               \* |
|             | Keras-Theano      |           \* |      \* |               \* |
| 02-15-2018  | FastAI            |        99.98 |    0.01 |               25 |
|             | Keras-Tensorfflow |        99.32 |      \* |               \* |
|             | Keras-Theano      |           \* |      \* |               \* |
| 02-16-2018  | FastAI            |       100.00 |    0.00 |               16 |
|             | Keras-TensorFlow  |        99.84 |      \* |               \* |
|             | Keras-Theano      |           \* |      \* |               \* |
| 02-22-2018  | FastAI            |        99.87 |    0.15 |              110 |
|             | Keras-TensorFlow  |        99.97 |      \* |               \* |
|             | Keras-Theano      |           \* |      \* |               \* |
| 02-23-2018  | FastAI            |        99.92 |    0.00 |              120 |
|             | Keras-TensorFlow  |        99.94 |      \* |               \* |
|             | Keras-Theano      |           \* |      \* |               \* |
| 03-01-2018  | FastAI            |        87.00 |    0.00 |                5 |
|             | Keras-TensorFlow  |        72.20 |      \* |               \* |
|             | Keras-Theano      |           \* |      \* |               \* |
| 03-02-2018  | FastAI            |        99.97 |     .01 |               75 |
|             | Keras-TensorFlow  |        98.12 |      \* |               \* |
|             | Keras-Theano      |           \* |      \* |               \* |
| ===         | ===               |          === |     === |              === |
| Multiclass  | Keras-TensorFlow  |        94.73 |      \* |               \* |
|             | Keras-Theano      |           \* |      \* |               \* |
|             | FastAI            |           \* |      \* |               \* |
| Binaryclass | Keras-TensorFlow  |        94.40 |      \* |               \* |
|             | Keras-Theano      |           \* |      \* |               \* |
|             | FastAI            |           \* |      \* |               \* |

### FastAI Results

#### Summary Results

| Data File      | Accuracy |    Loss |
| -------------- | -------: | ------: |
| 02-14-2018.csv |   99.99% | 0.00212 |
| 02-15-2018.csv |   99.86% | 0.02500 |
| 02-16-2018.csv |   99.97% |  324160 |
| 02-22-2018.csv |   99.97% | 0.00221 |
| 02-23-2018.csv |   99.82% | 0.06295 |
| 03-01-2018.csv |   87.14% | 0.37611 |
| 03-02-2018.csv |   99.72% | 0.85127 |

#### Confusion Matrices

|                                                      02-14-2018                                                      |                                                      02-15-2018                                                      |                                                      02-16-2018                                                      |
| :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------: |
| ![](<./graphics/confusion_matrices/02-14-2018--6-15(1).png>) | ![](<https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/02-15-2018--6-24(1).png>) | ![](<https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/02-16-2018--6-15(1).png>) |
|                                                      02-22-2018                                                      |                                                      02-23-2018                                                      |                                                      03-01-2018                                                      |
| ![](<https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/02-22-2018--6-15(1).png>) | ![](<https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/02-23-2018--6-15(1).png>) | ![](<https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/03-01-2018--6-15(1).png>) |

03-02-2018
![](<https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/03-02-2018--6-15(1).png>)

| Data File  | % of Attack Samples | % Attacks Flagged Correctly | % Benign Flagged Incorrectly |
| ---------- | ------------------: | --------------------------: | ---------------------------: |
| 02-14-2018 |                  36 |                         100 |                          <=1 |
| 02-15-2018 |                   5 |                          98 |                            0 |
| 02-16-2018 |                  57 |                         100 |                          <=1 |
| 02-22-2018 |                 <=1 |                           1 |                            0 |
| 02-23-2018 |                 <=1 |                          62 |                          <=1 |
| 03-01-2018 |                  28 |                          73 |                           10 |
| 03-02-2018 |                  27 |                         100 |                          <=1 |

### Using GPU

| Dataset     | Framework        | Accuracy (%) | Std-Dev | GPU Time (~mins) |
| ----------- | ---------------- | :----------: | :-----: | :--------------: |
| 02-14-2018  | FastAI           |      \*      |   \*    |        \*        |
|             | Keras-TensorFlow |              |   \*    |        \*        |
|             | Keras-Theano     |      \*      |   \*    |        \*        |
| 02-15-2018  | FastAI           |              |         |                  |
|             | Keras-TensorFlow |              |   \*    |        \*        |
|             | Keras-Theano     |      \*      |   \*    |        \*        |
| 02-16-2018  | FastAI           |              |         |                  |
|             | Keras-TensorFlow |              |   \*    |        \*        |
|             | Keras-Theano     |      \*      |   \*    |        \*        |
| 02-22-2018  | FastAI           |              |         |                  |
|             | Keras-TensorFlow |              |   \*    |        \*        |
|             | Keras-Theano     |      \*      |   \*    |        \*        |
| 02-23-2018  | FastAI           |              |         |                  |
|             | Keras-TensorFlow |              |   \*    |        \*        |
|             | Keras-Theano     |      \*      |   \*    |        \*        |
| 03-01-2018  | FastAI           |              |         |                  |
|             | Keras-TensorFlow |              |   \*    |        \*        |
|             | Keras-Theano     |      \*      |   \*    |        \*        |
| 03-02-2018  | FastAI           |              |         |                  |
|             | Keras-TensorFlow |              |   \*    |        \*        |
|             | Keras-Theano     |      \*      |   \*    |        \*        |
| ===         | ===              |     ===      |   ===   |       ===        |
| Multiclass  | Keras-TensorFlow |              |   \*    |        \*        |
|             | Keras-Theano     |      \*      |   \*    |        \*        |
|             | FastAI           |      \*      |   \*    |        \*        |
| Binaryclass | Keras-TensorFlow |              |   \*    |        \*        |
|             | Keras-Theano     |      \*      |   \*    |        \*        |
|             | FastAI           |      \*      |   \*    |        \*        |

# References

1. Iman Sharafaldin, Arash Habibi Lashkari, and Ali A. Ghorbani, “Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization”, 4th International Conference on Information Systems Security and Privacy (ICISSP), Portugal, January 2018
