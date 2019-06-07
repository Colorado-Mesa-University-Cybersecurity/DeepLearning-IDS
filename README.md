# DeepLearning-IDS

Towards Developing a Network Intrusion Detection System using Deep Learning Techniques

## Dataset

-   Orginial dataset downloaded from: https://www.unb.ca/cic/datasets/ids-2018.html
-   once the dataset was downloaded using AWS CLI as instructed by the source, there were 7 csv files that were preprocessed and labelled data

## Data cleanup

-   dropped rows with Infinitiy values
-   some files had repeated headers; dropped those
-   separated data based on attack types for each data file

## Dataset summary

| File Name      | Benign - FTP-BruteForce | SSH-Bruteforce | DOS-GoldenEye | DoS-Slowloris | DoS-SlowHTTPTest | DoS-Hulk | BruteForce-Web | BruteForce-XSS | SQL-Injection | Infilteration | Bot Attack | Total Attack |
| -------------- | ----------------------- | -------------- | ------------- | ------------- | ---------------- | -------- | -------------- | -------------- | ------------- | ------------- | ---------- | ------------ |
| 02-14-2018.csv | 663808                  | 193354         | 187589        | 0             | 0                | 0        | 0              | 0              | 0             | 0             | 0          | 0            | 380943 |
| 02-15-2018.csv | 988050                  | 0              | 0             | 41508         | 10990            | 0        | 0              | 0              | 0             | 0             | 0          | 0            | 52498 |
| 02-16-2018.csv | 446772                  | 0              | 0             | 0             | 0                | 139890   | 461912         | 0              | 0             | 0             | 0          | 0            | 601802 |
| 02-22-2018.csv | 1042603                 | 0              | 0             | 0             | 0                | 0        | 0              | 249            | 79            | 34            | 0          | 0            | 362 |
| 02-23-2018.csv | 1042301                 | 0              | 0             | 0             | 0                | 0        | 0              | 362            | 151           | 53            | 0          | 0            | 566 |
| 03-01-2018.csv | 235778                  | 0              | 0             | 0             | 0                | 0        | 0              | 0              | 0             | 0             | 92403      | 0            | 92403 |
| 03-02-2018.csv | 758334                  | 0              | 0             | 0             | 0                | 0        | 0              | 0              | 0             | 0             | 0          | 286191       | 286191 |
| -------------- | ----------------------- | -------------- | ------------- | ------------- | ---------------- | -------- | -------------- | -------------- | ------------- | ------------- | ---------- | ------       |
| Total          | 5177646                 | 193354         | 187589        | 41508         | 10990            | 139890   | 461912         | 611            | 230           | 87            | 92403      | 286191       | 1414765 |
