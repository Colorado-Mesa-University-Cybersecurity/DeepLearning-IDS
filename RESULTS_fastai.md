# Fast.ai Results Details

`Note that this document is still under development and tests are being ran`

## Brief Results
 - These are not updated...  
 
| Data File | Accuracy | Loss |
| --------- | -------- | ---- |
| 02-14-2018.csv | 99.99% | 0.050000
| 02-15-2018.csv | 99.99% | 0.050000
| 02-16-2018.csv | 99.99% | 0.050000
| 02-22-2018.csv | 99.99% | 0.050000
| 02-23-2018.csv | 99.99% | 0.050000
| 03-01-2018.csv | 85.00% | 0.050000
| 03-02-2018.csv | 99.99% | 0.050000

### Confusion Matrices
 02-14-2018 | 02-15-2018 | 02-16-2018
 :---------:|:----------:|:----------:
 ![](https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/02-14-2018--6-15(1).png) | In Progress | ![](https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/02-16-2018--6-15(1).png)  
 02-22-2018 | 02-23-2018 | 03-01-2018
 ![](https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/02-22-2018--6-15(1).png) | ![](https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/02-23-2018--6-15(1).png) | ![](https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/03-01-2018--6-15(1).png)
 03-02-2018 
 ![](https://github.com/rambasnet/DeepLearning-IDS/blob/master/graphics/confusion_matrices/03-02-2018--6-15(1).png) 
 
 
 | Data File | % of Data == Attacks | % Attacks Flagged Correctly | % Benign Flagged Incorrectly |
 |-----------|----------------------|-------------------|------------------|
 | 02-14 | 36 | 100 | <=1 |
 | 02-15 | n/a | n/a | n/a |
 | 02-16 | 57 | 100 | <=1 |
 | 02-22 | <=1 | 1 | 0 |
 | 02-23 | <=1 | 62 | <=1 |
 | 03-01 | 28 | 73 | 10 |
 | 03-02 | 27 | 100 | <=1 |
 

## Observations/Questions

### **Q1:** Why are these accuracy results extremely high?
#### **Hypothesis:** The models are overfit.
 
#### Training Data Size/Content Make-up

### **Q2:** Why are accuracy results significantly lower for `03-01-2018.csv`?
#### **Hypothesis:** The infiltration data in this file is extremely difficult to detect. 
